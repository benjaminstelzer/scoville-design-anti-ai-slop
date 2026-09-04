# W-005 qualification-v5 sealed readiness

Date: 2026-09-03  
State: blocked only at the explicit sealed-call authorization and private
custodian binding boundary  
Holdout unsealed: no  
Sealed calls made: zero

## Completed public and model-free prerequisites

- Design manifest:
  `3D19CE209E52AFCE91B888D6FB489E29EA9846A1442896129563D4B94ADC01C2`.
- UI manifest:
  `FD255A274E2D92C6DDA14CAD2A85FF0E7702960CEE6B2D3B9F20E04A78A78875`.
- Qualification-v5 job contract: 25 of 25 synthetic tests.
- Matrix: 156 registered, six quarantined, 150 runnable executions.
- Planned arm-balanced execution: 75 two-job case-by-repeat shards.
- Public v5 Terra High arm-parity canary: passed in both arms after Call B;
  four model responses, zero retries, no holdout access.
- Package, route, generated-index, Design/UI boundary, manifest, Skill Creator
  and native Plan validation: passed.

## Sealed custody integrity

The encrypted archives and opaque manifests were hashed without decrypting or
reading holdout content. All four values match the accepted custody receipt:

| Artifact | SHA-256 |
| --- | --- |
| Tranche 1 encrypted archive | `3884433D5C10FAB8763730C7F001501438620DC6A61D9F6CB4C53E67B9796BB7` |
| Tranche 1 opaque manifest | `4834FF6970A59D6826F951B24795A77409BAE0D80187333D3BD10565D85B4FCF` |
| Tranche 2 encrypted archive | `5EB1E116329125D6F880C71E7DE72C4E44C11CCC46B406F03E258EA0F62485F3` |
| Tranche 2 opaque manifest | `5C54B6542206DCCCF58AC29E6145AC35CFA98069E90FD060036E81B210850531` |

No case prompt, fixture, Gold record, grader or decryption key was opened.

## Rejected historical runner

The qualification-v3 batch wrapper and source runner are historical evidence,
not a v5 execution path. Their hashes are
`A598C07BBC8A4698F38DAB75A8453036FC5CFE887B28DB2E84A21A1BC77DFFB8`
and
`056A00B3B12D4150C8BDE4A9E70FF464CE35CCA54EF4B645434834E79EFDBABE`.
They target SOL XHigh, permit three parallel executions, bind obsolete package
inputs and have no independent Call-A/B/C versus transport-attempt state.
Reusing them would violate ADR-0013, ADR-0014 and ADR-0030 even if they still
executed successfully.

## Required private custodian binding

Before a real sealed call, the custodian must produce only armblind control
outputs:

1. the ordered 150-job and 75-shard schedule hash;
2. per-job text-versus-renderable classification without case disclosure;
3. preregistered canary job IDs covering each materially different arm and
   artifact path;
4. a runner manifest binding the current packages, Terra High, prompts,
   schemas, CLI, renderer, parser, scorer, fonts and v5 call-slot contract;
5. zero-call synthetic pass receipts for each materially different sealed
   materialization, parse, render, score and repair path;
6. a zero-call authorization receipt naming the first canary shard.

The custodian must keep prompts, fixtures, Gold, responses, artifacts and
scores private. The parent receives only hashes, aggregate progress and the
predeclared infrastructure status classes.

## Authorization boundary

ADR-0014 still requires separate explicit authorization for custodian unseal,
the first real sealed canary call and continuation beyond a successful canary
batch. The user's standing acceptance of internal Decisions and the advisory
resource-budget clarification do not grant that authority. Installation,
publication, commit, push, tag and release also remain unauthorized.

Until that authorization is given, W-005 may report readiness and the public
v5 evidence only. It cannot claim sealed qualification or proceed to aggregate
scoring or human-review packets.
