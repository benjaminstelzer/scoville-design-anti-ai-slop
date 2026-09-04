# Professional reference Plan review bundle

Date: 2026-09-02  
Status: frozen W-013 review input  
Files: 48  
Aggregate SHA-256: `62CBB5A4F04537B33B7094447DD1B72D4FB25F71C9AE723BFCEFC058F842401B`

## Aggregate algorithm

1. Resolve each path below beneath `Z:/Projekts/AI`.
2. Compute uppercase SHA-256 for the exact file bytes.
3. Sort records by absolute Windows path using PowerShell `Sort-Object`.
4. Normalize path separators in the record to `/`.
5. Join `relative/path|HASH` records with LF and no terminal LF.
6. Compute SHA-256 of the UTF-8 record sequence.

This bundle freezes review input only. The executable Design references remain
RC7 and the UI package remains the current ownership-only routing repair.

## File manifest

```text
scoville-design-anti-ai-slop/docs/audits/0002-professional-reference-depth-audit.md|FAF194C5D6D5D1140356D7FF46A2DCBBEA054374C4EEFCE4B7B3F43056C709EE
scoville-design-anti-ai-slop/docs/decisions/0015-require-professional-depth-before-final-qualification.md|60230DEAAE5DD6717A0819622D81029EBB71C3A4BD00B668A86E6C41CDF02C2D
scoville-design-anti-ai-slop/docs/decisions/0016-prioritize-latin-typography-with-a-multiscript-safety-floor.md|A16BEF11C7CDA1ED865C8A74E146B7DB3B5B24B8E911711BC7B13799C20030D1
scoville-design-anti-ai-slop/docs/decisions/0017-adopt-professional-depth-successor-module-map.md|CAF09EB120242FCFD166365DE5D82304504C299E2A83FE70DD5F6006DF665123
scoville-design-anti-ai-slop/docs/decisions/0018-separate-medium-intent-and-keep-spacing-with-its-relationship.md|897707003789B65FDA65B61CC347C7B652E1A88BE12E052D5E7C17F09A13A741
scoville-design-anti-ai-slop/docs/decisions/0019-use-local-rules-with-offline-source-provenance.md|B645DF9F5CB98C14FDD061682DF4198F894D324C9A2E66C7EE0719601E1687C2
scoville-design-anti-ai-slop/docs/plans/0001-build-and-qualify-scoville-design.md|C6835E26A1B8C611AF3681B85472F17B71BB655DA5DE94D1D9618A47478DAF1B
scoville-design-anti-ai-slop/docs/research/adoption-priority.md|1B4147569111BB02306EE6E9594BF39069C6379511039766685C329DFFA66521
scoville-design-anti-ai-slop/docs/research/canonical-curriculum-ledger.md|6EFA76EDC5E76488C565F7B6061F58937690B9900FDF5D6CEDE4FB664815D96D
scoville-design-anti-ai-slop/docs/research/medium-architecture-question.md|1AE416D8C5CE5A3E860354B111BB252543EDBDBD3670FA75C9FF36B96A7FF788
scoville-design-anti-ai-slop/docs/research/reference-audits/brand-and-visual-systems.md|072A8301F3F5CCC4D4E86753DD6E1C124AEA650C35A4E41281C3BE956760F1F0
scoville-design-anti-ai-slop/docs/research/reference-audits/brief-and-concept.md|68DC44006A325CB802D9DCD1559425E0B523DB44F54231C44A9EFA2A71E24938
scoville-design-anti-ai-slop/docs/research/reference-audits/colour-and-reproduction.md|40D8F401F6BD4695FBE4E1B7349819201EC776A532DE0B8B9D7A12D51F73E336
scoville-design-anti-ai-slop/docs/research/reference-audits/composition-and-layout.md|B5F1F513B19551AC99AC105ABE0A320577E1ECC15964F75E9B466BA73B571737
scoville-design-anti-ai-slop/docs/research/reference-audits/critique-and-validation.md|F427C078217CE5C8AD41B4E3E5B74F0257A7474BE1ECAD74E71E3A3B997F5EBA
scoville-design-anti-ai-slop/docs/research/reference-audits/culture-ethics-and-provenance.md|C3CF75C253550D9DBEFB52F2E73F0BEE9BF22572A675D0327C8B540D72689B68
scoville-design-anti-ai-slop/docs/research/reference-audits/imagery-and-art-direction.md|6AD303F0CEE6D7772D584B513953795A7AD0989E3F7BA14642E1CC8631ABDBCC
scoville-design-anti-ai-slop/docs/research/reference-audits/information-and-data.md|96FD1B127D835F9B5138055F79EBF49AC22BA67BA9140EFBA52F1C6C98AB534D
scoville-design-anti-ai-slop/docs/research/reference-audits/media-production-and-handoff.md|97DB496F1E86AA252FF6B166F92284F851B540DFDE42AE673C3AA3E26380CDEF
scoville-design-anti-ai-slop/docs/research/reference-audits/motion-and-sequence.md|0B1BABDD864EC4C16DF4118BBDF1F99772BE09C72D0A0CED43FAD4AA41A25158
scoville-design-anti-ai-slop/docs/research/reference-audits/sources-and-attribution.md|A0CDBAC7BA76065EADCC5317228FC863FB21CF7DB63078DB1308BC277D6BE548
scoville-design-anti-ai-slop/docs/research/reference-audits/style-direction.md|688C0566441380F89C30CFA3CCAC24CAA6F33BD380882000832B73FE634840F8
scoville-design-anti-ai-slop/docs/research/reference-audits/typography-and-writing-systems.md|61566F34F078882E622354BEDA1F42CCE156E1E6696615A06286BD4FF2450A24
scoville-design-anti-ai-slop/docs/research/reference-audits/ui-and-interaction-design.md|E6F1BDDE9A033FC24058C964843D381A3E04497CF84A2C2DADA6FDF102C1645D
scoville-design-anti-ai-slop/docs/research/successor-module-registry.md|B35E2D9A8974F8A0C1572E4C9D99A068ADFE7AE53BB4733838B17682AEEC4D74
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/brand-and-visual-systems.md|EB9715ABACF0F6A9AF448AA7A1EF13F5F253BE2BD32B7F8A4364B90A1A7EA293
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/brief-and-concept.md|0C8F6C977B8046FD007C5D572CC3F595A821776C7E64923FE8F521DEB9F3D509
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/colour-and-reproduction.md|BBCA8B1DC7D4D0DC9AE95F496CCE378850BF3DDDB04278B8DF95F7CB8ADAA6B7
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/composition-and-layout.md|263FF423F7A2BD6E4A6ED28EFC13F182786C3C53DE5793C8F328D9F3F2AF7D1F
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/critique-and-validation.md|8BE81DBE4A606554D362807961CE72CDAFB6CE3CF82A3D60BE36A2E176EEE510
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/culture-ethics-and-provenance.md|99E1238F53DF1F714F1C9A7A45E31096E772A3A9C82170ABFE9EEE291C1574B0
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/imagery-and-art-direction.md|A83F8BE010843205AEE730EF1E3B1B19B8A8F7D46DB9696D7D47F3687E3C268A
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/information-and-data.md|A8091BD6EC7396D86760892BDA5B3B141757CCE030197B27E381787BD5128ACE
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/media-production-and-handoff.md|976878C6FF61D3721B40808A32F42ADC3185242C1DA4C5A263B227E0FE2E2D66
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/motion-and-sequence.md|34A177757A4A93ED1EF1D71EB36611C9EE0DB2C9C019D55394C1498F74D06F27
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/sources-and-attribution.md|0DCB66E24A408E30CB7200B1CDAFCD4E228D4220A715B319FA893E8F3FEAF209
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/style-direction.md|EBD11BC75437EDE2A4F4ADA93002C6B8D814E62AA6B7F870466B727D8F215B98
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/typography-and-writing-systems.md|B26801BF7404FC9343FEC0319223129276DC9A33AB6768159728C0066CF1A54D
scoville-design-anti-ai-slop/docs/research/top-skill-comparisons/ui-and-interaction-design.md|F532930015FECA47E04DB919A13D9B2CCFBD2CCD0EE3C4B4C60B07AB9FF4EFC2
scoville-design-anti-ai-slop/docs/research/typography-rule-questions.md|FA32A08B77E23C2593F84FC3F673F273B8B511BF6340B53353C163EA5486F480
scoville-design-anti-ai-slop/docs/reviews/0004-fable-reference-depth-review.md|31D0EEC92A6C06DAA2B93D4FB96BF216376796D504F96DBE1C34F2137D95F480
scoville-design-anti-ai-slop/modules.yaml|7AB89C91E27C7216A1DE7BCB10F28EFE533F3FC4B48473375E495918EC9AC5EE
scoville-design-anti-ai-slop/SKILL.md|D9BB604B9CBE1E212AEDD13D1D2220E22C49AB46741332E60515DCBA24B6E3DF
scoville-ui-anti-ai-slop/docs/design-composition-evidence.md|FC027CC49567DE358CD59F9E5AB63799067CA83DE02D0525C865A722A41A6D0E
scoville-ui-anti-ai-slop/scoville-ui-anti-ai-slop/references/framework-alignment.md|73A5ECF950DA8FC797F6D065EFE876027651CC35D690263064E4968C76E71C3F
scoville-ui-anti-ai-slop/scoville-ui-anti-ai-slop/references/ui-quality.md|B14F89B01F58D639D6F127FD1E11F10D49A5B0B958CA040A06494EE22D1585B8
scoville-ui-anti-ai-slop/scoville-ui-anti-ai-slop/references/validation.md|9EDB6C49667133BAFAAA70B4FEA8FB73298FE11DE2DF5E544C34D21C809B3374
scoville-ui-anti-ai-slop/scoville-ui-anti-ai-slop/SKILL.md|C785BABF95B600A503C0BA80DB349A915628997ED15AA133FE6A1D9A93D47554
```

## Review target

Reviewers must return `READY` or concrete findings classified as Blocker, High,
Medium, or Low. Every finding must name the path, mechanism, impact, and
smallest correction. The review must cover professional completeness, forgotten
generalist capabilities, rule and source epistemics, module independence,
selective routing, Design/UI/production/source ownership, typography,
composition, spacing, style, responsive and fixed media, implementation order,
early-fail Terra testing, SkillOpt, and claim ceilings.

