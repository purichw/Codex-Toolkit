---
name: account-recovery-key
description: Design, audit, document, or implement generic account recovery-key flows for signup, forgot-password reset, and signed-in regeneration. Use when a project needs recovery codes/keys, recovery ID, password reset without email, drawer/account-settings regeneration, recovery hash storage, invalidating old recovery keys, or reusable auth guidance across Firebase, Supabase, custom auth, or local-first apps.
---

# Account Recovery Key

Use this skill to create a provider-neutral recovery-key pattern. Keep it
generic unless the user explicitly asks for Firebase, Supabase, or another
provider-specific implementation.

## Core Contract

- Generate a recovery key during account creation.
- Show the raw key immediately after signup and ask the user to save it.
- Store a verification hash, not only the raw key.
- Let signed-in users regenerate the key from account settings, profile drawer,
  or security settings.
- Regeneration invalidates the old key.
- Password reset with a recovery key must generate and reveal a new key.
- Do not add recovery-key behavior silently to high-stakes apps without
  rate-limiting, audit logging, and a clear display policy.

## Recommended Data Shape

Use equivalent fields for the target stack:

```json
{
  "accountIdentifier": "normalized-login-name-or-user-id",
  "recoveryKeyHash": "server-side-hash-or-hmac",
  "recoveryKeyIssuedAt": 1784050000000,
  "recoveryKeyVersion": 1
}
```

If recovery lookup uses a separate username/email lookup record, store or mirror
the recovery hash there too.

## Key Format

Use a cryptographically secure random generator. Prefer a human-readable key:

```text
XXXX-XXXX-XXXX
```

Use an alphabet that avoids ambiguous characters:

```text
ABCDEFGHJKLMNPQRSTUVWXYZ23456789
```

Normalize input by trimming, uppercasing, and removing spaces/dashes before
verification.

## Hashing Rule

Minimum:

```text
hash(normalizedAccountIdentifier + ":" + normalizedRecoveryKey)
```

Better for production:

```text
HMAC(serverSecret, normalizedAccountIdentifier + ":" + normalizedRecoveryKey)
```

Do not log raw keys. Do not send raw keys to analytics. Do not expose hashes to
untrusted clients when the backend can verify them server-side.

## Signup Flow

1. Validate signup fields and duplicate-account rules.
2. Generate recovery key.
3. Hash recovery key using the chosen hash rule.
4. Create the auth credential and profile/account record.
5. Store `recoveryKeyHash`, `recoveryKeyIssuedAt`, and optional version.
6. Show the raw recovery key in a prominent confirmation view.
7. Offer copy-to-clipboard.
8. Continue onboarding only after the user confirms they saved it when product
   risk warrants that friction.

## Forgot-Password Reset Flow

1. Ask for account identifier, recovery key, and new password.
2. Normalize account identifier and recovery key.
3. Look up the account or login record.
4. Hash submitted recovery key and compare with stored hash.
5. On mismatch, fail cleanly and apply throttle/rate-limit policy.
6. On match, reset or rotate the auth credential.
7. Generate a new recovery key.
8. Store the new recovery hash and issued timestamp.
9. Invalidate the old key by replacing the hash.
10. Show the new raw key and ask the user to save it.

## Drawer Or Settings Regeneration

Use when the user is already signed in.

1. Provide `Regenerate recovery key` in a trusted account surface.
2. Generate a new key and hash.
3. Persist the new hash and issue timestamp.
4. Replace local/session account mirror if the app has one.
5. Reveal the new raw key immediately.
6. Explain that the old key no longer works.
7. Offer copy-to-clipboard.

Display policy must be explicit:

- Small/private convenience mode: drawer may display and copy the current raw
  key if the product accepts that tradeoff.
- Hardened mode: drawer shows status/date only and reveals only newly generated
  keys.

Bias to hardened mode for public, financial, medical, enterprise, or sensitive
apps.

## Security And UX Checklist

- Recovery attempts are rate-limited or throttled.
- Wrong key has a generic error message.
- Successful reset/regeneration records an audit event when the app has audit
  logs.
- Old key is invalid after reset/regeneration.
- New key is shown after reset/regeneration.
- Copy button handles clipboard failure gracefully.
- User can return to login after reset.
- The flow works on mobile and does not depend on hover-only UI.
- Sensitive apps consider email confirmation, second factor, or admin-assisted
  recovery instead of recovery-key-only reset.
- When the task includes a visible signup, reset, drawer, settings, or recovery
  UI, use `$snapshot` automatically before the final response. Do not wait for
  the user to ask. If no fresh UI snapshot can be captured, state what visual
  evidence was used and what risk remains.

## Implementation Guidance

When implementing in a codebase:

1. Find the auth boundary, user/profile record, login lookup record, and account
   settings/profile drawer.
2. Add the smallest fields needed to existing account data contracts.
3. Keep the recovery-key reveal UI inside existing signup/reset/settings flows.
4. Preserve routes, permissions, form behavior, data contracts, and responsive
   layout.
5. Capture `$snapshot` evidence for visible recovery-key flows before the final
   response when UI was changed or audited.
6. Add tests for signup reveal, wrong-key failure, reset success, old-key
   invalidation, regeneration, and mobile rendering.

Do not create a new account/security product surface unless the project already
has an established settings/profile area or the user explicitly asks for one.
