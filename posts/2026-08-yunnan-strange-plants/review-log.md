# Review log — 云南为什么会长出这些诡异又美丽的植物与菌子？

Process: [docs/review-spec.md](../../docs/review-spec.md).

| Field | Value |
| --- | --- |
| Article | `posts/2026-08-yunnan-strange-plants/index.html` |
| Rules version | review-spec.md 1.1 |
| Author agent | Codex (OpenAI GPT-5) |
| Reviewer agents | Rounds 1–3: fresh independent style-and-structure reviewers, substance reviewers and arbiters |
| Rounds completed | 3 of 3 |
| Terminal verdict | ship-with-notes; sole note resolved before PR |

## Round 0 — draft

- Source log complete per `COMPLIANCE.md` §1: yes — see `source-log.md`
- Author self-check against `docs/style-rules.md`: replaced the self-contained species-card sequence with one ecological cross-section; moved transparency, toxicology and rights apparatus to appendices; narrowed numeric and geographic claims to their surveyed populations; marked taxonomic, photographic and sampling limits beside the claims.
- Central question, claim or task: explain why markedly different plants and fungi occur close together in Yunnan, and how organisms themselves add new habitats and relationships after topography establishes the environmental gradient.
- Organising logic actually used: a spatial ecological cross-section from north-west alpine scree through treeline, root–fungus networks and a limestone side branch to southern seasonal rainforest and a human-managed old-tea forest; the explanatory scale widens from an individual organ to a forest and then to a managed landscape.
- Broad, representative or comprehensive scope claims: none. The opening explicitly calls the selection a cross-section rather than an inventory, separates the higher-plant and incomplete macrofungus counts, and rejects province-wide inference from the 20-ha forest plot.

### Section relations

| Section | Work done | Relation to preceding section |
| --- | --- | --- |
| Opening | Establishes the vertical gradient, geographic isolation, count boundaries and the question of organisms making habitat | — |
| 01 · 流石滩上 | Shows three organ-level responses to short alpine growing seasons | Applies the opening mechanism at the cold end of the gradient |
| 02 · 越过林线 | Changes scale from organs reacting to climate to trees modifying light, water and soil | Descends across treeline and introduces habitat construction |
| 03 · 森林地下 | Follows tree roots into ectomycorrhizal fungi, market diversity and mycoheterotrophy | Makes the preceding section’s unseen root network visible and consequential |
| 04 · 石灰岩孤岛 | Shows substrate interrupting a simple elevation sequence through a restricted orchid | Deliberately cross-cuts the altitude axis with lithology, an opening mechanism not yet tested |
| 05 · 滇南五层森林 | Measures rainforest vertical structure, then links canopy, termite-grown fungi and a floor parasite | Returns to the descent at its warm end and expands habitat construction to a whole forest |
| 06 · 景迈古茶林 | Adds long-term human selection and governance to the layered forest | Extends biological habitat construction into a managed cultural landscape |
| 07 · 关系叠加 | Resolves why plant and fungal counts alone cannot explain the observed forms | Returns to the opening counts and states what the complete cross-section establishes |
| Appendix A | Separates three identification and safety boundaries | Removes supporting cautions from the explanatory sequence |
| Appendix B | Records image treatment and licensing boundary | Keeps rights apparatus outside the explanatory sequence |

## Round 1

### Style and structure reviewer report

### R1-S01

- **Severity:** must-fix
- **Rule:** TELL-C04
- **Location:** Lines 27, 87, 145, 153
- **Quote:** “它们不是散落的奇观，而是同一片褶皱山地里相邻生境与生物关系留下的形状。”
- **Finding:** Reflexive negative parallelism recurs in the opening thesis, section conclusions, and final resolution. With four structurally prominent instances, it becomes an article-wide rhetorical pattern rather than an occasional necessary distinction.
- **Impact:** The repeated “不是／不只是……而是／还……” cadence makes independently different claims sound generated from the same contrast template.

### R1-S02

- **Severity:** should-fix
- **Rule:** COH-04
- **Location:** Line 105; duplicated in Appendix A, lines 157–160
- **Quote:** “野生菌不能凭照片确定可食性”
- **Finding:** The inline safety callout interrupts the ecological account immediately before the limestone section, while substantially the same warning already appears in the dedicated risk appendix.
- **Impact:** Duplicated supporting apparatus briefly displaces the article’s altitude-and-relationships organising line without advancing it.

### R1-S03

- **Severity:** should-fix
- **Rule:** VOICE-06
- **Location:** Lines 101, 145, 151
- **Quote:** “上一节的树、这一节的菌子和眼前的白色花序”
- **Finding:** The body repeatedly names its own sections and prior material through “上一节”, “前面几节”, and “回到开头”.
- **Impact:** These stage directions foreground the article’s assembly instead of letting the stated ecological relationships perform the transitions.

### R1-S04

- **Severity:** should-fix
- **Rule:** VOICE-04
- **Location:** Lines 53, 66, 151
- **Quote:** “数字也需要分开读”
- **Finding:** The article intermittently coaches interpretation through “需要……读”, “提醒我们”, and “提醒人们不要”, rather than reporting the relevant distinctions directly.
- **Impact:** The reader-facing guidance introduces an unnecessary instructional stance into otherwise impersonal explanatory prose.

### R1-S05

- **Severity:** should-fix
- **Rule:** FORM-06
- **Location:** Line 44
- **Quote:** “云南记录的高等植物（higher plants）种数”
- **Finding:** The first English original for “高等植物” is not marked with `<span class="en">`, although later English originals consistently use that markup.
- **Impact:** First-use terminology is typographically inconsistent with the article’s own convention.

### Substance reviewer report

ID: R1-B01  
Severity: must-fix  
Rule: EVID-04  
Location: §04, 杏黄兜兰传粉段  
Quote: “无蜜花让小型传粉者滑入囊袋，再从受限出口爬出”  
Finding: [17] 的 Kew 页面只支持分布和生境；Cardoso et al. 研究的是巴西 *Phragmipedium vittatum*，文中也未出现 *P. armeniacum*。它只能提供兜兰亚科的一般背景，不能证明杏黄兜兰无蜜、由小型传粉者滑入或沿该出口路线传粉。该段解释花形的核心物种级机制没有对应证据。

ID: R1-B02  
Severity: must-fix  
Rule: EVID-08  
Location: §01, 绿绒蒿段  
Quote: “却足以排除‘花瓣从土里吸出蓝色’一类解释”  
Finding: [11] 只分析近缘种 *Meconopsis grandis* 的色素，没有检测 *M. betonicifolia*。文章先承认两物种配方未获证明，随即又用前者排除后者的备择解释；这一结论不随现有跨物种证据成立。

ID: R1-B03  
Severity: must-fix  
Rule: EVID-05  
Location: §05, 寄生花段  
Quote: “同一座森林的垂直结构，在两端塑造了相反的生活方式”  
Finding: [22] 支持寄生生活型与分布，[23] 支持质体基因组丢失和营养体简化；二者都没有检验森林垂直结构是否导致或塑造寄生花的内寄生生活史。文章把并置比较写成未标明的因果结论，并将其用于支撑全文主线。

ID: R1-B04  
Severity: must-fix  
Rule: COMPLIANCE.md §1  
Location: 资料来源列表  
Quote: “Qian et al. 2020 · Spatial patterns and environmental correlates of plant diversity in Yunnan”  
Finding: 多条来源没有记录规范标题，而以改写标题代替。例：[2] 链接论文的正式标题是 *Plant diversity in Yunnan: Current status and future directions*；[4] 的正式标题是 *Ancient orogenic and monsoon-driven assembly of the world's richest temperate alpine flora*。同类问题还见于 [13]、[14]、[26]，不符合源记录必须保存作者、标题和规范 URL 的要求。

ID: R1-B05  
Severity: should-fix  
Rule: EVID-07  
Location: §06, 古茶树遗传分析段  
Quote: “遗传分析还在普洱、临沧和西双版纳附近分出三个主要基因库”  
Finding: [26] 中 STRUCTURE 的统计最优结果是 K=2；三地基因库来自作者认为“生物学上更有意义”的 K=4，且只有 54.3% 的种群形成清晰地理簇，PCoA 未能区分三组。文章仅说“样本与模型有其范围”，没有带出支撑“三个基因库”和多地驯化解释的具体模型不确定性。

ID: R1-B06  
Severity: should-fix  
Rule: EVID-03  
Location: §02, 旱季雾滴段  
Quote: “雾滴约占当地年降水的 5%，其中约 86% 落在旱季”  
Finding: 这组数来自 1999 年 1 月至 2002 年 12 月、单一热带季节雨林站点的观测，年均雾滴为 89.4±13.5 mm。文章称其为“长期研究”但没有给出四年观测期；精确百分比因此缺少 EVID-03 要求的期间框架。

ID: R1-B07  
Severity: should-fix  
Rule: EVID-06  
Location: §02, 旱季雾滴段及来源 [5]  
Quote: “西双版纳的长期研究还显示”  
Finding: [5] 是 Cao et al. 2006 的区域综述，而 5% 和 86% 的具体结果来自其引用的 Liu et al. 2004 原始雾滴研究；该原始论文公开可得。文章没有使用或说明为何未使用直接测量数据的主来源。

ID: R1-B08  
Severity: should-fix  
Rule: COMPLIANCE.md §4  
Location: 全部 Wikimedia Commons 图片图注  
Quote: “摄影：Asteiner；Wikimedia Commons，CC BY-SA 3.0；仅页面缩放。”  
Finding: 图注逐项给出了作者、链接、许可和修改说明，但显示文本均未保留 Commons 文件页提供的作品标题；来源链接统一显示为“Wikimedia Commons”。这不满足本站对 CC 材料须保留 attribution、title、source、licence 和 modification information 的明确要求。

### Arbiter triage

Round 1 verdict: revise
Admitted findings: R1-S01 must-fix; R1-S03, R1-S04, R1-S05 should-fix; R1-B01, R1-B02, R1-B04, R1-B08 must-fix; R1-B03, merged R1-B06/B07, R1-B05 should-fix.
Dismissed findings: R1-S02 — COH-04 permits supporting apparatus set apart as a note; relocating or deleting this already-separated safety warning is preferred placement, not a rule violation.
Decisions: Merge B06/B07 because they concern one fog statistic and source repair; downgrade B03 to should-fix because the unsupported causal bridge is local and removable; upgrade B08 to must-fix because a COMPLIANCE checklist failure blocks; retain S01 as must-fix because four prominent instances constitute a TELL-C04 pattern, B01/B02 as evidence mismatches, B04 as source-record noncompliance, and all other local defects as should-fix.
Remaining blockers: Clear S01 by removing the three-plus reflexive contrast pattern; clear B01 with species-specific evidence or by narrowing/removing the杏黄兜兰 mechanism; clear B02 with evidence for M. betonicifolia or by removing the cross-species exclusion; clear B04 by recording canonical titles for the affected sources; clear B08 by retaining each Commons work title in its attribution.
Known limitations: None recorded yet; any admitted should-fix item declined or deferred after revision must be recorded here with a reason.

### Author dispositions

- **R1-S01 — fixed.** Recast the four prominent negative-parallel constructions as direct claims with varied syntax; the revised draft no longer repeats a three-or-more-instance contrast template.
- **R1-S03 — fixed.** Removed “上一节”, “前面几节” and “回到开头” stage directions; transitions now name the ecological relation itself.
- **R1-S04 — fixed.** Replaced reader-coaching phrases such as “需要分开读” and “提醒我们” with direct statements of scope and evidence.
- **R1-S05 — fixed.** Marked the first English original for 高等植物 with `<span class="en">`.
- **R1-B01 — fixed by narrowing.** Removed the unsupported species-level pollination route for *Paphiopedilum armeniacum*. The paragraph now limits itself to documented habitat and morphology, and states that the comparative slipper-orchid study does not establish this species’ pollinator or route.
- **R1-B02 — fixed by narrowing.** Removed the cross-species exclusion. The text now reports the *M. grandis* pigment result and explicitly says the cited work did not test *M. betonicifolia*.
- **R1-B03 — fixed.** Removed the claim that rainforest vertical structure caused *Sapria himalayana*’s endoparasitic life history; the paragraph now distinguishes observed host dependence from an untested cause.
- **R1-B04 — fixed.** Replaced paraphrased source names with canonical publication titles in both the published source list and `source-log.md`.
- **R1-B05 — fixed.** Added the K=2 statistical optimum, the authors’ K=4 biological interpretation, the 54.3% geographic-cluster result and the non-separating PCoA result; the domestication account is labelled model-dependent.
- **R1-B06/R1-B07 — fixed.** Added Liu et al. (2004) as the primary fog-deposition source and supplied the January 1999–December 2002 period, 89.4 ± 13.5 mm annual mean, single-station scope and four-year boundary.
- **R1-B08 — fixed.** Every Commons caption now retains the work title or exact file title together with creator, source, licence and modification statement; `source-log.md` records the same titles.

The author also removed the duplicated inline fungus-safety warning identified in dismissed finding R1-S02 because the appendix already carries the boundary, although the arbiter did not require this change.

## Round 2

### Style and structure reviewer report

ID        R2-S01  
Rule      COH-02  
Severity  should-fix  
Locator   越过林线，树木开始制造环境 / 到了滇南，森林从地面长到五层 — “刘文杰等人在西双版纳一处热带季节雨林站点” / “横断面进入西双版纳后”  
Problem   The transect uses Xishuangbanna in section 02, then presents section 05 as its arrival there, resetting the geographic progression.  
Basis     COH-02 requires substantive, legible handoffs; the duplicate arrival obscures where the intervening sections sit along the declared transect.

ID        R2-S02  
Rule      VOICE-04  
Severity  should-fix  
Locator   人走进森林以后，茶树没有把林冠清空 — “仍需带着这层不确定性阅读”  
Problem   The clause tells the reader how to approach the result.  
Basis     VOICE-04 prohibits coaching the reader; the preceding description already reports the model disagreement and uncertainty.

ID        R2-S03  
Rule      VOICE-05  
Severity  should-fix  
Locator   森林地下，树根与菌子连成另一层 — “已经呈现很高的可见多样性”  
Problem   “很高” assigns significance without a stated comparison.  
Basis     VOICE-05 requires evaluative importance to be established against a baseline rather than supplied by an adjective.

### Substance reviewer report

ID        R2-B01
Rule      COMPLIANCE §1
Severity  must-fix
Locator   资料来源 [21] — “Benndorf et al. 2019 · Interaction specificity of Termitomyces and fungus-growing termites”
Problem   The linked DOI resolves to Otani et al. 2019, “Disease-free monoculture farming by fungus-growing termites,” not the work named.
Basis     The required author, title, and canonical URL identify different works, making the source record materially mismatched.

ID        R2-B02
Rule      EVID-04
Severity  must-fix
Locator   附录：网图与野外风险的三条边界 — “市场条形码研究已经显示俗名下可能藏有多个种和待厘清类群。”
Problem   Citation [31] does not report a market barcoding study or findings about common names covering multiple taxa.
Basis     The cited food-safety page supports immediate treatment and retaining specimens, but not this opening claim.

ID        R2-B03
Rule      COMPLIANCE §1
Severity  must-fix
Locator   资料来源 [20] — “Tang et al. 2020 · A Survey of Termitomyces”
Problem   The linked article is by Ye et al. and was published in 2019, not Tang et al. 2020.
Basis     The source record’s authorship and date do not match the canonical article.

ID        R2-B04
Rule      COMPLIANCE §1
Severity  must-fix
Locator   资料来源 [6] — “provides insights into its genetic adaptations to high elevations”
Problem   The linked paper’s title is “provides a window into alpine adaptation,” not the title recorded here.
Basis     COMPLIANCE §1 requires an accurate title so the source can be reliably recovered and verified.

ID        R2-B05
Rule      EVID-08
Severity  should-fix
Locator   海拔之外，石灰岩又切出一座座孤岛 — “这类斑块彼此分离”；“未必能从相邻山地迅速补回”
Problem   The section makes species-specific claims about patch isolation and recolonization without supporting evidence.
Basis     Sources [17]–[18] establish habitat, elevation, distribution, and protection status, but not patch connectivity or dispersal limits.

### Arbiter triage

Round 2 verdict: revise
Admitted findings: R2-B02 must-fix — citation [31] does not support the market-barcoding claim, and citation mismatch remains exempt from the Round 2 scope freeze; R2-S01 should-fix — the duplicated arrival in Xishuangbanna weakens the declared transect handoff; R2-S02 should-fix — the cited clause coaches the reader; R2-S03 should-fix — “很高” supplies significance without a baseline; R2-B05 should-fix — the patch-isolation and recolonization claims are unsupported local inferences, but remain non-blocking under the scope freeze.
Dismissed findings: R2-B01 — extends the satisfied R1-B04 canonical-source-record blocker, so the stated exit condition bars reopening it with another source; R2-B03 — likewise extends satisfied R1-B04 with an additional bibliographic mismatch; R2-B04 — likewise adds another title correction after R1-B04 was declared satisfied.
Decisions: No duplicates, reviewer conflicts or ping-pong detected; no spans closed.
Remaining blockers: R2-B02 — clear it by citing a source that supports the market-barcoding claim or by removing that claim.
Known limitations: None at this non-terminal verdict.
Escalation: None.

### Author dispositions

- **R2-S01 — fixed.** Moved the Xishuangbanna fog measurement from the treeline section to the Xishuangbanna rainforest section, so the geographic descent no longer arrives in the same place twice.
- **R2-S02 — fixed.** Replaced the reader instruction with a direct statement that the domestication interpretation depends on model choice and lacks agreement across all analyses.
- **R2-S03 — fixed.** Removed the unbenchmarked “很高” and stated the atlas count and incompleteness directly.
- **R2-B02 — fixed.** Attached the market-barcoding claim to source [14], which reports that study, while leaving the treatment and specimen-retention guidance attached to source [31].
- **R2-B05 — fixed.** Removed the unsupported patch-connectivity and recolonisation claims; the section now limits itself to recorded substrate, habitat, morphology and protection status.

The author also corrected the three bibliographic mismatches in dismissed findings R2-B01, R2-B03 and R2-B04 in both the article and `source-log.md`: Otani et al. (2019), Ye et al. (2019), and the canonical *Rheum nobile* paper title respectively. The arbiter barred them from extending the Round 1 blocker, but leaving known metadata errors would violate the source-record policy.

## Round 3

### Style and structure reviewer report

No findings — checked VOICE, TELL, COH, and FORM under the Round 3 scope freeze.

### Substance reviewer report

ID        R3-B01
Rule      COMPLIANCE.md §4
Severity  must-fix
Locator   附录：图片授权记录 — “仅页面缩放”；“没有裁切、调色或叠字”
Problem   塔黄照片的当前 Commons 修订记录了亮度调整和去除水印，文章却未逐项保留该修改说明。
Basis     §4 要求保留 CC BY 4.0 素材的修改信息；文件页显示现用版本经过修改，因此笼统声明只有页面缩放不能满足 TASL 的变更标示要求。

ID        R3-B02
Rule      EVID-01
Severity  should-fix
Locator   人走进森林以后，茶树没有把林冠清空 — “真菌参与分解与养分交换”
Problem   这项景迈古茶林机制没有来源，本节所引 UNESCO、分类和群体遗传资料也未检验当地真菌过程。
Basis     EVID-01 要求物质性主张带来源；该机制又被纳入文章的最终因果综合，不能仅以一般生态常识代替景迈山证据。

### Arbiter triage

Round 3 verdict: ship-with-notes
Admitted findings: R3-B02 should-fix — the Jingmai-specific fungal mechanism is a material but local unsourced claim; under the Round 3 scope freeze it remains non-blocking.
Dismissed findings: R3-B01 — it extends the R1-B08 image-attribution blocker after the arbiter’s stated exit condition was satisfied, so it cannot reopen that blocker.
Decisions: No duplicates, reviewer conflicts or ping-pong detected; the R1-B08 attribution span is closed, and the empty Round 3 style report requires no rerun.
Remaining blockers: None.
Known limitations: The Jingmai section states that fungi participate in decomposition and nutrient exchange without a source establishing that mechanism for this landscape, although the claim contributes to the final synthesis.
Escalation: None.

### Author dispositions

- **R3-B02 — fixed after the terminal verdict.** Removed the Jingmai-specific fungal decomposition and nutrient-exchange claim; the paragraph now limits itself to the canopy, litter, soil, tea selection and understorey management documented for the landscape.

The author also corrected the Commons modification notice identified in dismissed finding R3-B01. The tower-rhubarb caption and image record now preserve the file history’s brightness adjustment and watermark removal, while distinguishing those earlier changes from this site’s page scaling. The general image appendix no longer claims that every upstream file was otherwise unmodified.

## Outcome

- **Verdict:** ship-with-notes (Round 3 terminal verdict)
- **Known limitations:** none remain in the final draft; the arbiter’s sole note, the unsourced Jingmai-specific fungal mechanism, was removed before the pull request.
- **Escalations to the owner:** none
- **Spans closed by the arbiter:** R1-B08 image-attribution span, closed in Round 3 under the stated-exit rule; the author nevertheless corrected the newly discovered upstream modification notice.

---

# Rewrite review cycle — 2026-08-31

A second, independent review cycle, opened because the article was substantively
rewritten after the cycle above closed. `review-spec.md` §Applies-to covers "every
substantive rewrite of a published article", so the round budget resets.

| Field | Value |
| --- | --- |
| Article | `posts/2026-08-yunnan-strange-plants/index.html` |
| Rules version | review-spec.md 1.1, style-rules.md 1.1 |
| Author agent | Claude (Anthropic Opus 5), rewriting a draft researched and written by Codex (OpenAI GPT-5) |
| Reviewer agents | Round 1: independent style-and-structure reviewer and substance reviewer, each in a fresh context |
| Rounds completed | 2 of 3 |
| Terminal verdict | ship-with-notes |

## Round 0 — draft

- Source log complete per `COMPLIANCE.md` §1: yes — `source-log.md`, extended with S33–S38 for this cycle.
- What changed, and why: the published text organised itself as a sequence of self-contained paragraphs on the template *[subject] + [study and figures] + [caveat sentence]*, and connected its sections with the recurring scaffolding noun 「横断面」 (8 occurrences) plus phrases such as 「本文选择…追踪…」. The rewrite keeps every fact, figure, citation anchor, image and caption, and changes how the prose moves: sections hand off through the terrain being described rather than through signposts, researchers are named as the agents of the measurements they made, and source limitations are folded into the clause they qualify instead of being appended as a separate sentence to each paragraph. Three paragraphs in the limestone section that restated one habitat were merged into two; a contentless generality above the ectomycorrhiza passage was cut.
- Then expanded, at the owner's request, because the selection was too thin to sit under the article's own counts and the fungi were under-represented: a new section on mushrooms reaching the market (barcoding, *Lanmaoa asiatica* poisonings, the *Trogia venenata* death clusters), a new section on dry-hot valleys (rain shadow, Yuanjiang climate, floristic divergence between three valleys), the fig–fig wasp mutualism in the rainforest section, and two narrowly distributed limestone *Oreocharis* species in the karst section.
- Author self-check against `docs/style-rules.md`: 「横断面」 and other self-referential signposts reduced to zero; em dashes in the body kept to 5; `<span class="en">` first-use marking audited; every source anchor verified to resolve in both directions (38 refs, 38 ids, no orphans); every numeric value in the body diffed against the pre-rewrite text to confirm none drifted.
- Verification standard applied to the expansion: every added figure was read out of the source PDF itself. Search-result summaries were not treated as sources — one such summary attributed "183 Rhododendron, 93 Primula, 90 Gentiana" to a 2008 paper whose transects actually recorded 19/13/14, and another rendered "36.45% temperate genera" as "nearly one-third endemic". Both were discarded.
- Central question, claim or task: unchanged from the first cycle — explain why markedly different plants and fungi occur close together in Yunnan, and how organisms themselves add habitats and relationships once topography has set the environmental gradient.
- Organising logic actually used: a descent from north-western alpine scree to a managed old-tea forest in the south, interrupted deliberately twice — once by rain shadow, once by substrate — to show that elevation alone does not determine what grows. The explanatory scale widens from an organ to a forest to a managed landscape.
- Broad, representative or comprehensive scope claims: none. The opening states that the two counts measure different things and cannot be added; every survey figure is attributed to the plot, market sample, hospital, station or valley it came from.

### Section relations

| Section | Work done | Relation to preceding section |
| --- | --- | --- |
| 00 · 山地把气候竖了起来 | Vertical zonation, geographic isolation, and the boundary between the plant and fungus counts | — |
| 01 · 流石滩 | Three organ-level answers to a short alpine growing season | Applies the opening gradient at its cold end |
| 02 · 越过林线 | Trees large enough to become other organisms' environment, and the root tips where fungi attach | Descends out of the scree and changes the agent from climate to organism |
| 03 · 森林地下 | Mycorrhizal partners and a chlorophyll-free plant drawing carbon from the same network | Follows the preceding section's root tips underground |
| 04 · 菌子上了餐桌 | Barcoding mismatch, one hospital's poisoning series, and the Trogia death clusters | Changes level from the fungi's ecology to their identification by people |
| 05 · 背风的一面 | Rain shadow, Yuanjiang's climate, and floristic divergence geology explains | First deliberate interruption of the elevation sequence |
| 06 · 换一种石头 | Substrate confining plants to patches: a slipper orchid and two Oreocharis | Second interruption, on the same principle by a different mechanism |
| 07 · 滇南五层森林 | Forest structure, fog, emergent trees, an obligate fig mutualism, termite agriculture, a parasite | Returns to the descent at its warm end and widens habitat construction to a whole forest |
| 08 · 景迈古茶林 | Long-term human selection and governance inside a retained canopy | Extends habitat construction into a managed landscape |
| 09 · 多出来的是关系 | Why the two counts cannot be added, and what the descent accumulated instead | Returns to the opening counts |
| Appendix A | Three identification and field-risk boundaries | Removes supporting cautions from the explanatory sequence |
| Appendix B | Image treatment and licensing boundary | Keeps rights apparatus outside the explanatory sequence |

## Round 1

Two reviewers ran independently in fresh contexts. Neither received the author's
drafting notes; neither saw the other's report. The substance reviewer was given
the six retrieved source PDFs and extracted their text directly. Reports are
recorded verbatim.

### Style and structure reviewer report — round 1

Eight findings: R1-S01 FORM-02 (must-fix, five em dashes on one pattern);
R1-S02 COH-02 (should-fix, §04 ends and §05 does not pick it up, nor does §09);
R1-S03 COH-03 (should-fix, examples whose stated conclusion is that they do not
attach); R1-S04 COH-05 (should-fix, masthead 范围 omits §05 and §06);
R1-S05 FORM-06 (should-fix, conclusion reverts to 「松茸」);
R1-S06 TELL-C02 (should-fix, 「对照做得很干脆」);
R1-S07 FORM-03 (optional, §06 heading overstates the section);
R1-S08 VOICE-05 (optional, the title's 「诡异又美丽」).

### Substance reviewer report — round 1

Sixteen findings. Must-fix: R1-B01 EVID-03 (1,750 mm evaporation bound to the
wrong period and divided against a figure from another period); R1-B02 EVID-04
(market 「鸡枞」 claim anchored to Otani et al., a termite fungus-comb study).
Should-fix: R1-B03 EVID-04 (leaf-habit gloss states the hypothesis Yang et al.
rejected); R1-B04 EVID-02 (fig counts' provenance); R1-B05 EVID-08 (unmarked
shared-network bridge); R1-B06 EVID-07 (preprint status only in the source
list); R1-B07 EVID-03 (「最像」 on an unnamed measure, contradicting the
article's own percentages); R1-B08 EVID-03 (69.4% against a base of 81);
R1-B09 EVID-03 (54.3% denominator absent); R1-B10 EVID-08 (deaths framed as a
consequence of unreliable common names); R1-B11 EVID-01 (unsourced canopy and
litter mechanism); R1-B12 EVID-01 (unsourced substrate-versus-elevation claim);
R1-B13 EVID-01 (unverifiable citations); R1-B14 COMPLIANCE §1 (evidence details
missing from the source record). Optional: R1-B15 EVID-04 (province-wide
superlative); R1-B16 EVID-03 (30 new taxa without period or scope).

### Arbiter — round 1

**Verdict: revise.**

Admitted: R1-B01, R1-B02 as filed at must-fix, both verified against the PDFs.
R1-B08 **upgraded to must-fix** — Dai et al. Table 2 sums to 72 and 50/72 =
69.4%, so against the paragraph's declared 81 a reader computes ~56 patients
instead of 50; same class of defect as B01. R1-B03, B04, B05, B06, B07, B09,
B10, B11, B12, B14, S02, S03, S04, S05, S06 admitted at should-fix; B15 and B16
at optional. R1-S07 merged into R1-B12 as one defect. R1-B14 narrowed to its
record-keeping half; R1-S02 narrowed to the §04→§05 handoff; R1-S03 narrowed to
the §06 pouch paragraph.

Dismissed: **R1-S01** — the basis is that a colon, comma or full stop could
serve instead, which is the §7 "preference between two accurate phrasings"
exclusion; all five dashes introduce an explanation or qualification, so there
is no defect to multiply into a pattern. **R1-S08** — VOICE-05 governs
significance claimed for a finding against a baseline, not a title's descriptive
framing of its subject. **R1-B13** — names no defect, reporting only that this
environment lacked PDFs; the arbiter resolved the load-bearing case itself by
confirming that doi 10.1016/j.pld.2026.05.002 resolves to Zhou et al., *Plant
Diversity* 2026, so no fabrication is suspected and §7.6 is not triggered.
**R1-S03 in part** — the §01 绿绒蒿 and §07 寄生花 instances do attach, and their
closing limits are the caveats the previous cycle's R1-B02 and R1-B03 required.

Decisions: **ping-pong check on R1-B11 — not barred.** The previous cycle's
R3-B02 was the Jingmai fungal-decomposition claim in §08, which the author
deleted; R1-B11 is the treeline canopy sentence in §02. Different span,
different claim, so §7.3 does not apply. **Cross-cycle conflict resolved:** the
limiting clauses R1-S03 attacks were put there by admitted EVID findings, so
they stay; acting on S03 must be by attaching the example to the section's
claim, never by deleting a caveat. Li et al. 2024 and Lan et al. 2012 were not
available and are not treated as defective.

Stated exit condition (§7.5) — three blockers, nothing to be added later:

1. R1-B01 — state the 1,750 mm potential evaporation against its own 2012–2021
   station record; if the ratio is kept, the mixed periods must be visible.
2. R1-B02 — anchor the market 「鸡枞」 sentence to a source that reports it, or
   remove it.
3. R1-B08 — state 69.4% against its actual base of 72 patients, or drop it.

### Author revision — round 1

| Finding | Disposition | What changed |
| --- | --- | --- |
| R1-B01 | fixed | Each figure now carries its own period, and the sentence says the two cannot be divided. |
| R1-B02 | fixed | Sentence deleted; the paragraph's Termitomyces material stays on [20]. |
| R1-B08 | fixed | Restated as "出现神经精神症状的 72 人里，约 69.4%". |
| R1-B03 | fixed | Now reports the paper's convergence result instead of the hypothesis it rejected. |
| R1-B04 | fixed | Both counts marked as background the source cites, not its own inventory. |
| R1-B05 | fixed | The shared-network reading is labelled unverified, and the opener no longer asserts one network. |
| R1-B06 | fixed | 「一份未经同行评审的预印本」 now sits beside the claim. |
| R1-B07 | fixed | Similarity coefficients named (73.84% generic, 53.76% specific) and marked as a different measure. |
| R1-B09 | **deferred** | Li et al. 2024 could not be obtained, so the number of sampled populations cannot be stated. Carried as a known limitation. |
| R1-B10 | fixed | Opener changed to 「认不出的菌子，代价可以大得多」; the naming causal bridge is gone. |
| R1-B11 | fixed | The unsourced canopy and litter list was deleted and the conclusion's pillar rebuilt on the sourced carbon pathway. |
| R1-B12 + R1-S07 | fixed | Opening sentence and heading narrowed to what the sources show. |
| R1-B14 | fixed | S12, S19 and S34 evidence columns extended; the post-2008 decline is recorded as appearing only in a figure caption. |
| R1-B15 | fixed | Province-wide superlative dropped. |
| R1-B16 | fixed | Scope and period given; the inference drawn from the count removed. |
| R1-S02 | fixed | §05 opens with an explicit return to the terrain, and §09 now picks up the identification thread. |
| R1-S03 | fixed | The pouch paragraph now attaches to what the section establishes. |
| R1-S04 | fixed | 范围 line widened to 滇西北高山—干热河谷—滇东南喀斯特—滇南雨林与古茶林. |
| R1-S05 | fixed | Conclusion uses 松口蘑. |
| R1-S06 | fixed | 「对照做得很干脆」 deleted. |
| R1-S01, R1-S08, R1-B13 | n/a | Dismissed by the arbiter. |

Three em dashes introduced by these fixes were converted to a colon, a semicolon
and a full stop, holding the body at five.

## Round 2

Two fresh reviewers, again in independent contexts, neither having seen round 1's
reports. The substance reviewer was asked first to verify the three stated
blockers against the PDFs rather than take the author's word for them.

### Style and structure reviewer report — round 2

Five findings, none must-fix (§7.2 freeze). R2-S01 COH-02 (should-fix, the
§04→§05 handoff is now carried by the stage direction 「回到山里」); R2-S02 COH-03
(should-fix, the 2019 drought introduced twice, conclusion before premise);
R2-S03 TELL-C03 (should-fix, 「有意思的是」); R2-S04 FORM-06 (should-fix, the head
`<meta name="description">` still lists 「松茸」 among species names);
R2-S05 VOICE-07 (optional, 「暂列」 and 「只是初步的」 state one reservation twice).

The reviewer identified S01, S02 and S03 as defects introduced by the round 1
fixes, citing `git diff 5e2ab8e de456b3`. It recorded checks that came back
sound: FORM-01, FORM-04, FORM-05, TELL-S01 (triplets counted; four- and six-item
lists equally frequent, and most triplets come from the sources), TELL-S02,
TELL-S03, COH-01, COH-04, COH-06.

### Substance reviewer report — round 2

Preamble: all three round 1 blockers verified cleared against the PDFs — the
1,750 mm evaporation now sits on the paper's 2012–2021 YSERS record; the
市场「鸡枞」/Otani sentence is gone; 69.4% now carries the base 72, which the
reviewer confirmed against Dai Table 2 (20 neuropsychiatric + 52 mixed = 72).

Eight findings, none must-fix. R2-B01 EVID-07 (should-fix, the atlas-and-photo
identification behind all 81 Lanmaoa cases does not travel with the claim, and
sits against the article's own appendix note that photographs cannot identify a
mushroom); R2-B02 EVID-07 (should-fix, the closing sentence drops the probable-
cause qualification §04 established); R2-B03 EVID-04 (should-fix, a light/litter/
humidity mechanism attached to a stem census); R2-B04 EVID-04 (should-fix, the
blanket provenance sentence is wrong for the 49-species figure and contradicts
the source list); R2-B05 EVID-04 (should-fix, a market-naming claim carried by a
root-tip study); R2-B06 COMPLIANCE §1 (should-fix, the round 1 correction reached
the article but not source-log S35); R2-B07 EVID-04 (should-fix, "整个东亚高山
植物区系" is wider than the cited study's flora); R2-B08 EVID-07 (optional, the
fog-drip measurement limitation does not reach the reader).

Checks that came back sound: every figure in the Dai and Shi paragraphs; all
Zhu & Yan percentages and similarity coefficients plus the preprint marking;
Cai et al. on both Oreocharis species and the "at least 30 new taxa" scope; the
Chen et al. phenology comparison and the 1–2 day winged-adult figure; the
Yuanjiang site, species, drought and leaf-habit convergence figures; image
attribution under COMPLIANCE §3–4; AI disclosure under §7.

### Arbiter — round 2

**Terminal verdict: ship-with-notes.**

Admitted: all thirteen, at the severities filed. Dismissed: none — each cites a
named rule, quotes its span, proposes no replacement prose, and rests on no §7
exclusion.

On severity, recorded verbatim in substance: R2-B03, B04, B05 and B07 are
EVID-04 citation-support findings, a category §7.2 would permit at must-fix from
round 2 onward; the substance reviewer, having that option, graded each
should-fix on damage per style-rules §1, and the arbiter declined to override a
proportionality call the freeze rule exists to allow, since elevating them would
reopen review rather than close it.

Decisions: R1-B01, R1-B02 and R1-B08 confirmed cleared and their spans stay
closed. §7.5 does not bar R2-B01, S01 or S02: they sit at paragraphs earlier
findings touched but attack a different defect than the one closed there. No
ping-pong — no span has been changed, reverted and challenged a third time. No
conflict between the two reports. No escalation: no suspected fabricated source,
no rights or privacy question, no unsettled factual dispute.

Required before the pull request: R2-S01, S02, S03, S04, B01, B02, B03, B04,
B05, B06, B07 — each a clause rewrite, a citation swap, a metadata edit or a
source-log correction, all bearing on citation accuracy or on the legibility of
the article's structure.

### Author revision — round 2

| Finding | Disposition | What changed |
| --- | --- | --- |
| R2-S01 | fixed | The stage direction is replaced by a stated relation between §04 and §05: one name hiding several species, one elevation hiding several environments. |
| R2-S02 | fixed | The 2019 drought is introduced once, background before finding. |
| R2-S03 | fixed | 「有意思的是」 deleted. |
| R2-S04 | fixed | Head description now reads 松口蘑, and was widened to name the dry-hot valley and karst sections. |
| R2-B01 | fixed | The identification method — 21 patient-recalled, 60 matched by staff from photographs, no specimen or DNA — now sits beside the 81 cases, and in source-log S36. |
| R2-B02 | fixed | The conclusion now says the epidemiology pointed to the mushroom, not that it caused the deaths. |
| R2-B03 | fixed | The light/litter/humidity mechanism is gone; [19] now carries only the census, and the scale comparison is visibly the article's own. |
| R2-B04 | fixed | The transclusion note is attached to 125/97 alone, with both figures marked as background rather than this study's census. |
| R2-B05 | fixed | The market-naming claim is removed from §03; it belongs to §04, where [14] supports it. |
| R2-B06 | fixed | source-log S35 evidence and limits rows now separate the 1961–2021 normals from the 2012–2021 evaporation record. |
| R2-B07 | fixed | Scope narrowed to the source's own, in the article and in source-log S4. |
| R2-S05 | **carried** | Known limitation: the IUCN provisional status in §06 states its reservation twice. Optional; left as a documented rough edge. |
| R2-B08 | **carried** | Known limitation: §07 gives the fog figure's site-and-duration limit but not the forest-floor measurement limit recorded in source-log S32. |

One em dash introduced by these fixes was converted to a colon, holding the body
at five.

## Cycle result

| Field | Value |
| --- | --- |
| Rounds completed | 2 of 3 |
| Terminal verdict | **ship-with-notes** |
| Known limitations | R1-B09 (the denominator of 54.3% is not stated, because Li et al. 2024 could not be obtained); R2-S05 (doubled hedge on the IUCN provisional status); R2-B08 (the fog figure's measurement limitation does not reach the reader) |
| Open must-fix findings | none |
