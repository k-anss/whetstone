# Error Ledger

This is a living, cross-project failure taxonomy. Add project occurrences without embedding story-specific conclusions in core rules.

| ID | Failure family | Status | Detection question | First evidence |
|---|---|---|---|---|
| E001 | Invented core motive | hard | Is the claimed motive stated, or supported by two facts and labeled inference? | `孺子帝/chunk_001` |
| E002 | Third-party harm counted as focal cost | hard | Did the focal actor actually bear, risk, or surrender this cost? | `孺子帝/chunk_001` |
| E003 | Adjacent events stitched into a false exchange | hard | Can offer, concession, causal link, and response be located in order? | `孺子帝/chunk_001` |
| E004 | Surprise or fear mislabeled as expectation management | hard | Is a future expectation intentionally changed and tied to action? | `孺子帝/chunk_001` |
| E005 | Quote normalized, shortened, or concatenated | hard/mechanical | Does the exact continuous string occur in the allowed source slice? | `孺子帝/chunk_001` |
| E006 | Later benefit folded into earlier bargain | candidate | Was this benefit promised in the original exchange? | `孺子帝/chunk_001` |
| E007 | Open-ended future debt minimized | candidate | Is delayed payment being mistaken for low cost? | `孺子帝/chunk_001` |
| E008 | Decision attributed to the wrong actor | observe | Who made the verifiable choice, rather than merely appearing? | — |
| E009 | Ongoing action written as completed transformation | observe | What observable result exists inside the evidence boundary? | — |
| E010 | Same event counted through two lines | observe | Do problem, lever, and cost all differ? | — |
| E011 | Inference contradicts explicit narration | hard | Does the narrator explicitly say the act was accidental, unplanned, or unknown? | `孺子帝/chunk_001-v2` |
| E012 | Uncertainty upgraded to evidence contamination | hard | Does “needs more investigation” actually prove false, coerced, or polluted evidence? | `孺子帝/chunk_001-v2` |
| E013 | Chronology reversed into causality | hard | Had the alleged caused decision already occurred before this condition or action? | `孺子帝/chunk_001-v2` |
| E014 | Reviewer-suggested frame copied without re-proof | hard | Is the repair satisfying the reviewer's wording rather than the source evidence? | `孺子帝/chunk_001-v2` |
| E015 | Exact quote declared unavailable without source search | candidate | Was the source searched for a continuous shorter excerpt before leaving it blank? | `孺子帝/chunk_001-v2` |
| E016 | Wrong chapter anchor on a valid event | candidate | Do the listed chapters contain the initiating bargain and claimed result? | `孺子帝/chunk_001-v2` |
| E017 | Physical or emotional action upgraded into strategy | hard | Is there a supported objective, observable response, and no explicit accidental explanation? | `孺子帝/chunk_001-v2` |
| E018 | One-time help upgraded into loyalty or durable alliance | hard | What is the lowest relationship status supported by repeated behavior? | `孺子帝/chunk_002-guardrail` |
| E019 | Actor action linked directly to result without response | hard | What did the counterpart or system observably do between action and result? | `孺子帝/chunk_002-guardrail` |
| E020 | Proposal, adoption, execution, and result collapsed | hard | Who proposed, approved, executed, deviated, and produced the result? | `孺子帝/chunk_002-guardrail` |
| E021 | Narrated paraphrase rewritten as direct dialogue | hard | Is the quote exact direct speech, rather than narration of its meaning? | `孺子帝/chunk_001-v2` |
| E022 | Certainty substituted for comparison of explanations | candidate | What strongest rival explanation remains, and what evidence would distinguish it? | `孺子帝/chunk_002-guardrail` |
| E023 | Externally imposed safeguard credited to focal actor | hard | Who designed, controlled, and could alter the alleged retained option? | `孺子帝/chunk_002` |
| E024 | Broad destabilization intent assigned a precise result | hard | Was a target state defined before success or backfire was declared? | `孺子帝/chunk_002` |
| E025 | Independent downstream choice credited to prior persuader | hard | Was the later action agreed, or was it a third option chosen independently? | `孺子帝/chunk_002` |
| E026 | Passive rescue and later deliberate tactic merged | hard | Did agency, lever, counterpart, or cost change inside the chain? | `孺子帝/chunk_002` |
| E027 | High-value unconventional cost event omitted | candidate | Were deliberate pain, asset surrender, long debt, and enemy disposition scanned? | `孺子帝/chunk_002` |
| E028 | Self-check finding left unapplied | hard | What delete, downgrade, split, or rewrite followed the identified failure? | `孺子帝/chunk_003` |
| E029 | Same event dual-routed by viewpoint only | hard | Do problem, lever, and cost differ, or only the narrative angle? | `孺子帝/chunk_003` |
| E030 | Hypothetical or pre-existing reputation charged as paid cost | hard | What observable incremental loss occurred because of this action? | `孺子帝/chunk_003` |
| E031 | Admitted paraphrase retained in quote field | hard/mechanical | Is the field exact and continuous regardless of its disclaimer? | `孺子帝/chunk_003` |
| E032 | Lack of prior knowledge reframed as deliberate tolerance | hard | Did the manager know and choose not to intervene before failure? | `孺子帝/chunk_003` |
| E033 | Access strategy credited with target's independent appearance | hard | Is only access proven, or did the target respond because of it? | `孺子帝/chunk_003` |
| E034 | Chunk boundary expanded to finish an arc | hard | Did the producer read or cite any chapter after the assigned end? | `孺子帝/chunk_004-rejected` |
| E035 | Symbolic elevation mislabeled as hostage control | hard | Can the actor restrict exit and condition release or disposition? | `孺子帝/chunk_004-rejected` |
| E036 | Generic future management burden charged as current cost | hard | What concrete resource, opportunity, obligation, or action was already surrendered? | `孺子帝/chunk_004-rejected` |
| E037 | Placeholder framework submitted as completed extraction | hard/mechanical | Does any output contain empty chapters, generic “this chunk” prose, or pending-detail markers? | `孺子帝/chunk_007-019` |
| E038 | Title scan substituted for full-text event recall | hard | Does the chapter-by-chapter coverage record show source reading beyond titles? | `孺子帝/chunk_006` |
| E039 | Incomplete batch reported as completed | hard | Do completion claims agree with each file's own draft and reading-status declarations? | `孺子帝/chunk_006-019` |
| E040 | Explicit causal denial ignored | hard | Does narration assign the response to someone else or say the focal actor made no effort? | `孺子帝/chunk_005-A02` |
| E041 | Malformed card polished instead of re-extracted | hard | Was the replacement rebuilt from source events, with permission to change title, route, and count? | `孺子帝/R2-reextract` |
| E042 | Limited-goal action lacks success and stop conditions | hard | Are the replacement target, observable threshold, and stopping rule all explicit? | `孺子帝/R2R-018-02` |
| E043 | Duplicate cards counted as independent method contexts | hard | How many distinct actor-action-response-result event nodes support the method? | `孺子帝/R3` |
| E044 | Coverage template rejected by validator | hard/mechanical | Does the parser accept both `第X章` and numeric chapter cells emitted by the template? | `skill-v2 audit` |
| E045 | Card cites chapter outside assigned range | hard/mechanical | Are all parsed card/event chapter references within the assigned boundaries? | `skill-v2 audit` |
| E046 | Quote found elsewhere in book passes validation | hard/mechanical | Is the quote inside the assigned chapter slice, not merely anywhere in the source? | `skill-v2 audit` |
| E047 | Six-question shell passes format validation | hard/mechanical | Are actor, dilemma, action, response, paid cost, and result all present and non-empty? | `skill-v2 audit` |
| E048 | Stop thresholds documented but not executed | hard/mechanical | Did the signing command run production mode with self-check, coverage, quote, and density gates? | `skill-v2 audit` |

## Update Rules

For each occurrence append to the project audit:

- chunk and card;
- exact faulty sentence;
- source contradiction or missing evidence;
- disposition;
- proposed general rule;
- whether producer self-check caught it.

Promote `candidate` after a second independent occurrence. Promote immediately when the error can fabricate evidence or corrupt event counts. Retire a rule when a broader rule and validator fully cover it.

Do not add a new hard rule for every bad sentence. Add one rule per failure mechanism.
