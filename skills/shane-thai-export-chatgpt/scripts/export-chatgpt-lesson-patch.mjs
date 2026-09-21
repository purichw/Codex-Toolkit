#!/usr/bin/env node
import fs from 'node:fs/promises'
import path from 'node:path'
import { createRequire } from 'node:module'
import { pathToFileURL } from 'node:url'

const defaultRepo = '/Users/point/Website Projects/thai-flashcards'

const sourceDataByUnitId = {
  'mc-structure-01': ['src/data/mainCourseStructure.ts'],
  'mc-greetings-01': ['src/data/mainCourseGreetings.ts'],
  'mc-numbers-01': ['src/data/mainCourseNumbers.ts'],
  'mc-time-01': ['src/data/mainCourseDailyLife.ts'],
  'mc-days-01': ['src/data/mainCourseDailyLife.ts'],
  'mc-monthyear-01': ['src/data/mainCourseDailyLife.ts'],
  'mc-classifiers-01-counting-everyday-things': ['src/data/mainCourseClassifiers.ts'],
  'mc-questions-01-question-particles': ['src/data/mainCourseQuestions.ts'],
  'mc-questions-02-open-questions': ['src/data/mainCourseOpenQuestions.ts'],
  'mc-requests-01-permission-favors': ['src/data/mainCourseRequests.ts'],
  'cumulative-main-course-u1-u7': ['src/data/mainCourseCumulative.ts'],
  'mc-location-01-where-is-it': ['src/data/mainCourseLocation.ts'],
  'mc-home-garden-01-around-the-house': ['src/data/mainCourseHomeGarden.ts'],
  'mc-food-kitchen-01-market-table': ['src/data/mainCourseFoodKitchen.ts'],
  'mc-adjectives-01-antonyms-comparisons': ['src/data/mainCourseAdjectives.ts'],
  'mc-transport-01-getting-around': ['src/data/mainCourseTransport.ts'],
  'mc-directions-01-asking-for-directions': ['src/data/mainCourseDirections.ts'],
}

const sharedPatchFiles = [
  'src/data/mainCourse.ts',
  'src/data/mainCourseClozeTests.ts',
  'src/data/mainCourseListeningTestData.ts',
  'src/data/mainCourseListeningTestMeta.ts',
  'src/data/mainCourseSceneFirstPlans.ts',
  'src/data/lessonFramework.ts',
  'src/main-course/mainCourseRoutes.ts',
  'src/main-course/mainCourseState.ts',
  'src/MainCourse.tsx',
  'src/CourseHome.tsx',
]

const currentTabs = [
  'overview',
  'dialogue',
  'cards',
  'read',
  'story',
  'grammar',
  'spelling',
  'quiz',
  'cloze',
  'listening',
]

function parseArgs(argv) {
  const options = {
    repo: defaultRepo,
    date: localDate(),
    out: null,
    overwrite: false,
  }

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index]
    if (arg === '--repo') options.repo = argv[++index]
    else if (arg === '--date') options.date = argv[++index]
    else if (arg === '--out') options.out = argv[++index]
    else if (arg === '--overwrite') options.overwrite = true
    else if (arg === '--help' || arg === '-h') {
      printHelp()
      process.exit(0)
    } else {
      throw new Error(`Unknown argument: ${arg}`)
    }
  }

  return options
}

function printHelp() {
  console.log(`Usage:
  node export-chatgpt-lesson-patch.mjs [--repo <path>] [--date YYYY-MM-DD] [--out <dir>] [--overwrite]

Defaults:
  --repo ${defaultRepo}
  --out  <repo>/docs/content-exports/chatgpt-lesson-patch-YYYY-MM-DD
`)
}

function localDate() {
  const now = new Date()
  const year = now.getFullYear()
  const month = String(now.getMonth() + 1).padStart(2, '0')
  const day = String(now.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}

function slugify(value) {
  return String(value)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
}

function clean(value) {
  return String(value ?? '').trim().replace(/\s+/g, ' ')
}

function mdList(values) {
  const items = (values ?? []).map(clean).filter(Boolean)
  return items.length ? items.join(', ') : 'none'
}

function normalizeAssetPath(value, repoRoot) {
  if (typeof value !== 'string' || !value.startsWith('file://')) return value
  const pathname = decodeURIComponent(new URL(value).pathname)
  const relative = path.relative(repoRoot, pathname)
  return relative.startsWith('..') ? value : relative
}

function normalizeForExport(value, repoRoot) {
  if (Array.isArray(value)) return value.map((item) => normalizeForExport(item, repoRoot))
  if (!value || typeof value !== 'object') return normalizeAssetPath(value, repoRoot)

  return Object.fromEntries(
    Object.entries(value)
      .filter(([, entryValue]) => entryValue !== undefined)
      .map(([key, entryValue]) => [key, normalizeForExport(entryValue, repoRoot)]),
  )
}

function jsonBlock(label, value, repoRoot) {
  return `### ${label}

\`\`\`json
${JSON.stringify(normalizeForExport(value ?? null, repoRoot), null, 2)}
\`\`\`
`
}

function ids(items) {
  return (items ?? []).map((item) => item.id).filter(Boolean)
}

function sectionIdSummary(unit) {
  const rows = [
    ['communication', ids(unit.communication)],
    ['dialogues', ids(unit.dialogues)],
    ['vocabulary', ids(unit.vocabulary)],
    ['readingWords', ids(unit.readingWords)],
    ['readingActivity', ids(unit.readingActivity)],
    ['spellingSkill', ids(unit.spellingSkill)],
    ['spellingBuilders', ids(unit.spellingBuilders)],
    ['spellingActivity', ids(unit.spellingActivity)],
    ['grammarSections', ids(unit.grammar?.sections)],
    ['story', ids(unit.story)],
    ['quiz', ids(unit.quiz)],
    ['clozeSections', ids(unit.clozeTest?.sections)],
    ['listeningSections', ids(unit.listeningTest?.sections)],
  ]

  return rows.map(([label, values]) => (
    `- ${label}: ${values.length ? values.map((id) => `\`${id}\``).join(', ') : 'none'}`
  )).join('\n')
}

function levelForUnit(unit, levels) {
  return levels.find((candidate) => {
    const [start, end] = candidate.unitOrderRange
    return unit.order >= start && unit.order <= end
  }) ?? null
}

function renderUnit(record, repoRoot, generatedDate) {
  const { unit, routeHash, level, sourceFiles, listeningTest } = record
  const unitWithListening = { ...unit, listeningTest }

  return `# ChatGPT Lesson Patch Packet: Unit ${unit.order} - ${unit.title}

Generated ${generatedDate}. This packet is for ChatGPT-assisted lesson patching. The source of truth remains the app source files, not this Markdown export.

## Quick Instructions For ChatGPT

1. Identify the exact section(s) to modify.
2. Preserve existing stable IDs unless replacement/deletion is explicitly requested.
3. If adding content, propose new IDs that match this unit's existing prefix pattern.
4. Keep Thai, Shane/course romanization, English, audio text, quiz answers, labels, tags, and group IDs aligned. Keep reference Paiboon/IPA aligned when those fields are present.
5. Write the actual revised lesson content yourself. Do not return only directions, placeholders, or instructions for Codex to author later.
6. Return finished replacement objects/arrays or a unified diff only for the relevant source file(s), plus a targeted patch plan.
7. For new learner-facing tabs/modules, use \`TAB_EXTENSION_PROTOCOL.md\` and return a proposal with fully authored target-unit content instead of pretending the tab already exists.

## Unit Metadata

| Field | Value |
| --- | --- |
| Unit ID | \`${unit.id}\` |
| Order | ${unit.order} |
| Title | ${unit.title} |
| Thai title | ${unit.thaiTitle ?? 'none'} |
| Route | \`${routeHash}\` |
| Status | ${unit.status} |
| Phase | ${unit.phase} |
| Level | ${level ? `${level.displayName} (\`${level.levelKey}\`)` : 'unknown'} |
| Goal | ${clean(unit.goal)} |
| Description | ${clean(unit.description) || 'none'} |
| Estimated minutes | ${unit.estimatedMinutes ?? 'none'} |
| Owner source file(s) | ${sourceFiles.map((file) => `\`${file}\``).join(', ') || 'unknown'} |

## Stable ID Map

${sectionIdSummary(unitWithListening)}

## Patch Surfaces

${jsonBlock('welcome', unit.welcome, repoRoot)}
${jsonBlock('overviewSections', unit.overviewSections, repoRoot)}
${jsonBlock('dialogues', unit.dialogues, repoRoot)}
${jsonBlock('communication', unit.communication, repoRoot)}
${jsonBlock('vocabulary', unit.vocabulary, repoRoot)}
${jsonBlock('readingWords', unit.readingWords, repoRoot)}
${jsonBlock('readingActivity', unit.readingActivity, repoRoot)}
${jsonBlock('story', {
    storyTitle: unit.storyTitle,
    storyFocus: unit.storyFocus,
    story: unit.story,
  }, repoRoot)}
${jsonBlock('grammar', unit.grammar, repoRoot)}
${jsonBlock('spelling', {
    spellingIntro: unit.spellingIntro,
    spellingSkill: unit.spellingSkill,
    spellingBuilders: unit.spellingBuilders,
    spellingActivity: unit.spellingActivity,
  }, repoRoot)}
${jsonBlock('quiz', {
    quizSettings: unit.quizSettings,
    quizAlwaysUnlocked: unit.quizAlwaysUnlocked,
    quiz: unit.quiz,
  }, repoRoot)}
${jsonBlock('clozeTest / Fill', unit.clozeTest, repoRoot)}
${jsonBlock('listeningTest', listeningTest, repoRoot)}
${jsonBlock('sceneFirstPlan', unit.sceneFirstPlan, repoRoot)}
${jsonBlock('designFramework / acceptance / qa', {
    designFramework: unit.designFramework,
    acceptanceCriteria: unit.acceptanceCriteria,
    qaMatrix: unit.qaMatrix,
  }, repoRoot)}
`
}

function renderReadme(records, generatedDate) {
  return `# ChatGPT Lesson Patch Export

Generated ${generatedDate}.

Purpose: make it easy for ChatGPT to patch Shane Thai learner lesson content without reading the React app or raw TypeScript first.

## What To Give ChatGPT

For a normal single-lesson patch:

1. \`README.md\`
2. \`PATCH_PROTOCOL.md\`
3. One unit file, for example \`unit-13-talk-around-the-house.md\`

For cross-unit sequencing or difficulty:

4. \`ALL_UNITS_COMPACT.md\`

For a possible new learner-facing tab/module:

5. \`TAB_EXTENSION_PROTOCOL.md\`
6. \`SOURCE_MAP.md\`

## Do Not

- Do not patch generated Markdown as source of truth.
- Do not change stable IDs casually.
- Do not add a new tab silently as a content-only patch.
- Do not remove or rename existing tabs unless the user explicitly asks.
- Do not respond with only directions, suggestions, placeholders, or instructions for Codex to write the lesson later.

## Prompt: Normal Patch

\`\`\`text
You are helping patch a beginner Thai lesson in the Shane Thai app.

Read README.md, PATCH_PROTOCOL.md, and the unit packet below.

Goal: [describe the change]

Important: write the actual revised lesson content yourself using the exported packet. Do not return only advice, directions, placeholders, or "Codex should write..." instructions.

Please respond with:
1. Diagnosis.
2. Exact stable IDs to keep, modify, add, or remove.
3. Finished replacement lesson content for every touched object/array, with Thai / Shane-course romanization / English / audio text / answers / tags aligned. Include reference Paiboon/IPA only where those fields already exist.
4. Minimal patch plan or source-file diff showing where that content should be applied.
5. Checks Codex should run after applying it.

Do not rewrite unrelated sections.
\`\`\`

## Prompt: New Tab Proposal

\`\`\`text
You are helping design a possible new learner-facing lesson tab for Shane Thai.

Read README.md, PATCH_PROTOCOL.md, TAB_EXTENSION_PROTOCOL.md, SOURCE_MAP.md, and the unit packet.

Goal: [example: add a Passage Reading tab to Unit 13]

Important: write the actual content for the target unit. Do not stop at a data model or instructions for Codex to compose the passage/questions later.

Please respond with:
1. Whether this should be a new tab or fit an existing tab.
2. Proposed section id, label, purpose, and tab order.
3. Data model and stable ID pattern.
4. Fully authored content for the target unit.
5. Implementation checklist for Codex.
6. Risks to progress, routing, completion, audio, images, and tests.
\`\`\`

## Exported Units

| Unit | ID | Title | Route | Owner | File |
| --- | --- | --- | --- | --- | --- |
${records.map(({ unit, routeHash, sourceFiles, fileName }) => `| ${unit.order} | \`${unit.id}\` | ${unit.title} | \`${routeHash}\` | ${sourceFiles.map((file) => `\`${file}\``).join('<br>')} | [${fileName}](./${fileName}) |`).join('\n')}
`
}

function renderPatchProtocol() {
  return `# Patch Protocol For ChatGPT

Use this for normal lesson content patches and existing-section restructuring.

## Response Shape

\`\`\`text
## Diagnosis
- What is wrong, missing, or out of sequence.

## Scope
- Unit:
- Source file(s):
- Sections touched:
- Change type: content-only / existing-section restructure / new tab proposal

## ID Plan
- Keep:
- Modify:
- Add:
- Remove:

## Authored Lesson Content
- Write the finished Thai / Shane-course romanization / English / prompts / answer keys / tags / metadata for every touched item. Include reference Paiboon/IPA only where those fields already exist.
- Do not hand back only directions, placeholders, or a to-do list for Codex.

## Patch
- Provide only the affected replacement objects/arrays, or a unified diff if asked, using the authored content above.

## Consistency Checks
- Thai, Shane/course romanization, English, audio, and answer keys aligned; reference Paiboon/IPA aligned when present.
- Quiz answers still match options.
- Listening audio text matches the intended prompt.
- Tags/labels/groupIds still make sense.
- Difficulty is i+1 relative to prior units.
\`\`\`

## Rules

- Preserve stable IDs by default.
- Prefer modifying specific objects over rewriting whole arrays.
- Author the revised lesson content in the response; Codex should apply and verify it, not invent it later.
- Keep lesson order, route, unit ID, progress keys, audio IDs, and image IDs stable unless explicitly asked.
- If a Thai phrase changes, update Shane/course romanization, English, audio text, quiz answer, cloze option, and any matching card/reading/story reference as needed. Update reference Paiboon/IPA when those fields are present.
- If the request adds a learner-facing tab or module, switch to \`TAB_EXTENSION_PROTOCOL.md\`.
`
}

function renderTabProtocol() {
  return `# Tab Extension Protocol For ChatGPT

Use this only when the requested patch may add a learner-facing tab or module, such as a future \`Passage Reading\` tab.

Even for a proposal, ChatGPT must write the actual target-unit lesson content. Do not return only a feature brief, content direction, or instructions for Codex to author later.

## Current Learner Unit Tabs

\`\`\`text
${currentTabs.join('\n')}
\`\`\`

Current route shape:

\`\`\`text
#/unit/<unit-slug>
#/unit/<unit-slug>/<section>
\`\`\`

## Files A New Tab Usually Touches

- \`src/main-course/mainCourseRoutes.ts\` for the \`MainCourseSection\` union and route parsing.
- \`src/data/mainCourse.ts\` for the unit data type.
- The unit owner source file for content.
- \`src/main-course/mainCourseState.ts\` for availability, progress, completion, and reset behavior.
- \`src/MainCourse.tsx\` for nav, rendering, next-step flow, and labels.
- \`src/CourseHome.tsx\` if dashboard/next-action/search behavior changes.
- \`src/data/contentContracts.test.ts\` and nearby progress/practice tests.
- Audio/image audit scripts if the new tab introduces new asset types.

## New Tab Proposal Shape

\`\`\`text
## New Tab Proposal
- Proposed section id:
- Display label:
- Learner purpose:
- Where it appears in the unit order:
- Lock/unlock behavior:
- Completion behavior:
- Progress tracking behavior:
- Reset behavior:
- Audio/image requirements:
- Affected source files:

## Data Model
- New field(s) on MainCourseUnit:
- Item shape:
- Required IDs:
- Optional metadata:

## Content For This Unit
- New stable IDs:
- Fully authored Thai:
- Fully authored Shane/course romanization:
- Fully authored English:
- Prompts / answer keys / notes:
- Notes:

## Implementation Checklist For Codex
- Route union updated.
- Unit type updated.
- Availability/progress/completion updated.
- MainCourse renderer/nav updated.
- Tests updated.
- Snapshot or browser check recommended.
\`\`\`

## Passage Reading Example

Do not force a new \`Passage Reading\` request into the existing \`read\` tab unless the user asks. Propose it as a new module:

\`\`\`text
section id: passage
display label: Passage
learner purpose: read a connected short passage after word-level Read, before Story or Grammar
data field: passageReading?: CoursePassageReading
item IDs: <unit-prefix>-passage-01, <unit-prefix>-passage-q-01
\`\`\`

## Guardrails

- Treat new tabs as product decisions.
- Fully author the MVP content for the requested unit; implementation notes alone are incomplete.
- Do not remove or rename existing tabs to make room.
- Preserve existing route behavior and progress data.
- Prefer additive data fields over changing existing object meanings.
- Start with one unit as an MVP unless the user asks for all units.
`
}

function renderSourceMap(records, generatedDate) {
  return `# Lesson Source Map

Generated ${generatedDate}.

## Shared Files

${sharedPatchFiles.map((file) => `- \`${file}\``).join('\n')}

## Current Main Course Tab Registry

Current \`MainCourseSection\` values:

${currentTabs.map((tab) => `- \`${tab}\``).join('\n')}

## Units

${records.map(({ unit, routeHash, level, sourceFiles, fileName }) => [
    `### Unit ${unit.order}: ${unit.title}`,
    `- Unit ID: \`${unit.id}\``,
    `- Route: \`${routeHash}\``,
    `- Level: ${level ? `${level.displayName} (\`${level.levelKey}\`)` : 'unknown'}`,
    `- Owner source: ${sourceFiles.map((file) => `\`${file}\``).join(', ')}`,
    `- Export file: \`${fileName}\``,
  ].join('\n')).join('\n\n')}
`
}

function renderCompact(records, generatedDate) {
  return `# All Units Compact Context

Generated ${generatedDate}. Use this for cross-unit context before patching a single lesson.

${records.map(({ unit, routeHash, level, sourceFiles }) => {
    const keyCards = (unit.communication?.length ? unit.communication : unit.vocabulary)
      .slice(0, 12)
      .map((item) => `${item.thai} (${item.paiboon}) = ${item.english}`)
      .join(' ; ')
    const counts = {
      communication: unit.communication?.length ?? 0,
      dialogues: unit.dialogues?.length ?? 0,
      vocabulary: unit.vocabulary?.length ?? 0,
      readingWords: unit.readingWords?.length ?? 0,
      story: unit.story?.length ?? 0,
      grammarSections: unit.grammar?.sections?.length ?? 0,
      quiz: unit.quiz?.length ?? 0,
      cloze: unit.clozeTest?.sections?.length ?? 0,
      listening: unit.listeningTestId ? 1 : 0,
    }
    return [
      `## Unit ${unit.order}: ${unit.title}`,
      `- ID: \`${unit.id}\``,
      `- Route: \`${routeHash}\``,
      `- Level: ${level ? level.displayName : 'unknown'}`,
      `- Owner: ${sourceFiles.map((file) => `\`${file}\``).join(', ')}`,
      `- Goal: ${clean(unit.goal)}`,
      `- Description: ${clean(unit.description) || 'none'}`,
      `- Reading focus: ${mdList(unit.readingFocus)}`,
      `- Story title: ${unit.storyTitle ?? 'none'}`,
      `- Counts: ${Object.entries(counts).map(([key, value]) => `${key}=${value}`).join(', ')}`,
      `- Key cards: ${keyCards || 'none'}`,
    ].join('\n')
  }).join('\n\n')}
`
}

async function resolveOutputDir(baseDir, overwrite) {
  if (overwrite) return baseDir
  try {
    await fs.access(baseDir)
  } catch {
    return baseDir
  }

  for (let index = 2; index < 100; index += 1) {
    const candidate = `${baseDir}-${index}`
    try {
      await fs.access(candidate)
    } catch {
      return candidate
    }
  }
  throw new Error(`Could not find available output directory after ${baseDir}-99`)
}

async function main() {
  const options = parseArgs(process.argv.slice(2))
  const repoRoot = path.resolve(options.repo)
  const generatedDate = options.date
  const baseOutputDir = options.out
    ? path.resolve(options.out)
    : path.join(repoRoot, 'docs/content-exports', `chatgpt-lesson-patch-${generatedDate}`)
  const outputDir = await resolveOutputDir(baseOutputDir, options.overwrite)

  const requireFromRepo = createRequire(path.join(repoRoot, 'package.json'))
  const vitePath = requireFromRepo.resolve('vite')
  const { createServer } = await import(pathToFileURL(vitePath).href)

  const server = await createServer({
    root: repoRoot,
    logLevel: 'error',
    server: { middlewareMode: true },
    appType: 'custom',
  })

  try {
    const [mainCourse, levelsModule, routeModule, listeningModule] = await Promise.all([
      server.ssrLoadModule('/src/data/mainCourse.ts'),
      server.ssrLoadModule('/src/data/mainCourseLevels.ts'),
      server.ssrLoadModule('/src/main-course/mainCourseRoutes.ts'),
      server.ssrLoadModule('/src/data/mainCourseListeningTestData.ts'),
    ])

    const units = mainCourse.readyMainCourseUnits.slice().sort((a, b) => a.order - b.order)
    const records = units.map((unit) => {
      const sourceFiles = sourceDataByUnitId[unit.id] ?? []
      const routeHash = routeModule.getMainCourseRouteHash(unit.id)
      const level = levelForUnit(unit, levelsModule.mainCourseLevels)
      const fileName = `unit-${String(unit.order).padStart(2, '0')}-${slugify(unit.title)}.md`
      const listeningTest = listeningModule.mainCourseListeningTestsByUnitId[unit.id]
      return { unit, sourceFiles, routeHash, level, fileName, listeningTest }
    })

    await fs.rm(outputDir, { recursive: true, force: true })
    await fs.mkdir(outputDir, { recursive: true })

    for (const record of records) {
      await fs.writeFile(
        path.join(outputDir, record.fileName),
        renderUnit(record, repoRoot, generatedDate),
        'utf8',
      )
    }

    const combined = [
      renderReadme(records, generatedDate),
      '\n---\n',
      ...records.map((record) => `\n---\n\n# ${record.fileName}\n\n${renderUnit(record, repoRoot, generatedDate)}`),
    ].join('\n')

    await fs.writeFile(path.join(outputDir, 'README.md'), renderReadme(records, generatedDate), 'utf8')
    await fs.writeFile(path.join(outputDir, 'PATCH_PROTOCOL.md'), renderPatchProtocol(), 'utf8')
    await fs.writeFile(path.join(outputDir, 'TAB_EXTENSION_PROTOCOL.md'), renderTabProtocol(), 'utf8')
    await fs.writeFile(path.join(outputDir, 'SOURCE_MAP.md'), renderSourceMap(records, generatedDate), 'utf8')
    await fs.writeFile(path.join(outputDir, 'ALL_UNITS_COMPACT.md'), renderCompact(records, generatedDate), 'utf8')
    await fs.writeFile(path.join(outputDir, 'all-units-content.md'), combined, 'utf8')

    console.log(JSON.stringify({
      outputDir,
      relativeOutputDir: path.relative(repoRoot, outputDir),
      units: records.length,
      files: records.length + 6,
    }, null, 2))
  } finally {
    await server.close()
  }
}

main().catch((error) => {
  console.error(error)
  process.exitCode = 1
})
