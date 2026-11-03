# Default infrastructure region

Owner preference, 2026-11-03 (Asia/Bangkok). Apply when choosing a region for new
projects or regional resources, or planning an explicitly requested migration.
This is a default for this owner's projects, not a universal hosting rule.

## Choose and record the region

1. **Choose Thailand first** when the actual service supports it with the needed
   capabilities on the approved plan.
2. Otherwise choose the **closest suitable supported Asian region to Thailand**.
   Singapore is a common candidate, not a hardcoded substitute for checking the
   provider's current service-specific availability and region identifiers.
   Use latency evidence when available; do not invent performance measurements.
3. Set the region explicitly in provisioning/deployment configuration where the
   provider permits it. Do not silently accept US/Europe, an ambiguous automatic
   location, or a provider's preselected default.
4. Choose database, regional storage and request-serving backend/functions
   together. Keep chatty compute close to its primary data dependency, preferably
   in the same supported Thailand/Asian region; otherwise use the closest
   compatible placement and document the topology. Moving only functions near
   users while leaving their database far away can add cross-region latency.
5. Record the chosen provider region identifiers, database/backend relationship
   and rationale in the project's infrastructure/runbook and handoff context.
   A later explicit project-specific user choice overrides this default.

Check each service's current documented regions and the actual account/plan
options before creation. A provider's CDN presence in Bangkok does not establish
that its database or functions can run there. Global CDN delivery and build-runner
locations are distinct from the runtime/data region; do not force global delivery
into a single location or claim a build location proves runtime placement.

## Existing systems and exceptions

- Inspect existing deployed database/backend placement before changing anything.
  This preference does not authorize migration, deletion/recreation, credential
  changes, resource creation, deployment, or a new paid plan by itself.
- Preserve an already explicit decision to retain an existing region. For a new
  function attached to an existing remote database, follow that approved
  topology instead of separating compute from data merely to label it Asian.
  Propose a coordinated migration only within the requested scope.
- If required features, data-location requirements or approved-plan limits make
  Thailand/Asia unavailable, explain the concrete constraint and obtain any
  missing decision before choosing a non-Asian region or increasing cost. Do not
  treat a free-project quota as permission to buy a plan or delete another project.
  Do not repeat approval for an exception the user already explicitly decided.

## Scoped verification

For new infrastructure or region/config changes, check both explicit configuration
and actual provisioned/deployed region metadata for the intended resource/revision.
After an authorized deployment, verify the relevant runtime and data targets;
a successful build alone is insufficient. Report intentional exceptions and
unverified placement. For an unrelated code release, preserve the known topology;
this preference does not require a migration, broad latency audit or extra deploy.
