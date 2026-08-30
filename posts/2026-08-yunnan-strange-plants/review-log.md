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
