# Playbook: AI-Powered SEO Content Production
### An SOP for creating, structuring, and distributing content for AI-mediated search (Google AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini)

**Author:** Vaishnavi
**Based on:** 10 practitioner sources (see `research/sources.md`), collected May–June 2026
**Scope:** B2B SaaS content teams, small-to-mid size, adapting an existing content function for AI-mediated discovery.

---

## How to read this document

Every actionable recommendation below is cited to a specific source. Where I found real disagreement between practitioners, I've called it out explicitly rather than smoothing it over — that section is arguably more useful than the checklist itself. I've also flagged what I deliberately left out, one idea that's mine and not sourced from anyone, and where I think this playbook is weakest.

---

## Part 1 — The Production SOP

### Step 1: Research before writing

Before producing anything, run three parallel research tracks:

- **Query fan-out mapping.** For a given topic, generate the 25–30 related sub-queries an LLM would actually branch into when answering a broader question, not just the head keyword. iPullRank's own tool (Q4) does this using Gemini's API (source: Garrett Sussman, [E Coffee with Experts interview](https://www.youtube.com/watch?v=UMHaeT6Ou94), 29.08.2025). Kevin Indig's clickstream data backs up why this matters: in AI Mode specifically, 88% of users accept the model's shortlist and 64% click nothing at all — meaning if your content isn't already synthesized into the answer, a click-through recovery strategy won't save you (source: Kevin Indig, [LinkedIn post](https://www.linkedin.com/in/kevinindig/), 05.2026).
- **Off-platform demand research.** Don't rely on keyword-tool search volume alone — check where the actual conversation volume is happening. Ross Simmonds gives a concrete example: a keyword tool showed ~800 monthly searches for a gardening sub-topic, but the equivalent YouTube videos had 455,000 combined views — a much stronger signal of real demand (source: Ross Simmonds, [Content Distribution in the Age of AI](https://www.youtube.com/watch?v=VXxFJAg7YJw), 08.10.2025).
- **Citation-source mapping.** Before writing, check which types of sources are already being cited for your target queries (forums, review sites, YouTube, docs) using a tool like Profound or Peec, so you know what format you're actually competing against — not what you assume you're competing against (source: Ross Simmonds, same source as above).

### Step 2: Structure every page for passage-level retrieval

AI systems retrieve specific passages or "chunks," not whole pages — a page can rank well overall and still never get cited if the specific section that answers the question is weak.

- Keep each passage **semantically tight and self-contained**: one clear concept per passage, understandable without needing the surrounding sections. Aleyda Solis's example: "What is technical SEO?" answered in one focused, well-structured paragraph is citable; a paragraph that jams technical SEO, link building, and content strategy together is not (source: Aleyda Solis, [The AI Search Optimization Roadmap](https://www.youtube.com/watch?v=BjyF_4UhoOM), 09.09.2025).
- Use accessible, well-formatted HTML (clear headings, no critical content locked behind JS rendering an AI crawler can't execute) — Garrett Sussman notes that if your content requires JS rendering a bot can't process, "you are not going to be visible" regardless of quality (source: Garrett Sussman, cited above, 29.08.2025).
- Add table of contents, FAQ blocks, and "key takeaways" sections — Glenn Gabe's citation-source analysis found these structural enhancements correlated with higher inclusion rates (source: Glenn Gabe, [Google's December 2025 Broad Core Update](https://www.youtube.com/watch?v=8hWV3DVSRf0), 23.12.2025).
- Write in simple subject-predicate-object sentence structure ("semantic triples") where possible — this is a linguistics-level readability signal that helps LLMs parse relevance, separate from keyword matching (source: Garrett Sussman, cited above).
- Target passage-level relevance scores of roughly 60–80% cosine similarity to your target query using a relevance-checking tool — 100% would just mean you repeated the query itself, which reads as unnatural (source: Garrett Sussman, cited above).

### Step 3: Ground every page in real expertise, not just structure

Structure gets you retrievable; it doesn't get you trustworthy. Several sources converged hard on this point:

- Feature a real, named author with demonstrable expertise; include verifiable facts and specific data rather than generic claims (source: Aleyda Solis, cited above).
- Original insight matters more than production polish — "the more you're just leaning on tools to do the thinking for you, the more that that's going to not work over time" (source: Lily Ray, [The Future of SEO](https://www.youtube.com/watch?v=2htSIT0HLjs), 18.03.2026).
- If a page is AI-drafted, a human still needs to fact-check and vet it before publishing — AI content is probabilistic and will confidently state wrong things (source: Garrett Sussman, cited above).

### Step 4: Distribute beyond your own domain — deliberately, not everywhere at once

- Treat YouTube and Reddit as primary citation sources for AI Overviews and LLM answers, not afterthoughts — Ross Simmonds' team found Reddit had overtaken traditional B2B SaaS review sites (G2, Capterra, TrustRadius) as a citation source, while those review sites' organic traffic is declining (source: Ross Simmonds, cited above). Glenn Gabe's independent citation-source tracking supports the Reddit trend specifically: Reddit's share of ChatGPT citations grew from near-zero to over 5% following OpenAI's data partnership with Reddit (source: Glenn Gabe, cited above).
- On Reddit specifically, follow a staged approach: claim or co-moderate your brand subreddit, create a named brand-representative account (not a faceless corporate one), and post four content types — educate, engage, entertain, empower. Don't post links in your first five days on a subreddit; it reads as spam and gets you banned (source: Ross Simmonds, cited above).
- Repurpose long-form content into "micro-assets" across formats rather than treating each channel as a separate production job — one podcast episode can become clips, a blog post, and multiple LinkedIn posts (source: Ross Simmonds, cited above).

### Step 5: Track what you can, and accept what you can't

- Roughly 70% of brand mentions inside AI chat conversations are "dark" — no referral click, invisible to standard analytics (source: Ross Simmonds, [LinkedIn post](https://ca.linkedin.com/in/rosssimmonds), 04.2026). Pew Research data independently found only about 1% of users click through a citation in AI Overviews at all (source: cited by Kevin Indig, [SEO in the Age of AI podcast](https://www.youtube.com/watch?v=qujABKOAThA), 15.09.2025). Build reporting expectations around this limitation now, rather than discovering it during a stakeholder review.
- For content that does get clicked (engines like Perplexity and Gemini that do link out), fact-dense, numbers-heavy content performs better at earning the click than vague summaries (source: Ross Simmonds, cited above).

### Step 6: Treat volume as a risk factor, not a growth lever, once you scale

- Sites that scaled aggressively with lower-quality AI-generated content saw traffic surges followed by sharp drops once a core update landed — Glenn Gabe calls this the "Mt. AI" pattern (source: Glenn Gabe, [LinkedIn post](https://www.linkedin.com/in/glenngabe/), 25.05.2026). Quality oversight has to scale alongside volume, not lag behind it.

---

## Part 2 — Where experts disagree

### Disagreement 1: How aggressively to invest in Reddit

- **Ross Simmonds** recommends treating Reddit as a primary owned-adjacent channel: claim your brand subreddit, run a named brand account, post consistently across four content types, and even install a Reddit ad pixel for remarketing — calling it "low-hanging fruit" businesses are sleeping on (source: Ross Simmonds, cited above).
- **Eli Schwartz** is much more cautious. He calls Reddit-focused GEO tactics "dangerous," arguing that brands trying to manufacture presence on Reddit are "angering actual humans" who will retaliate publicly, and that whatever a brand does on Reddit "doesn't stay on Reddit" (source: Eli Schwartz, [Stop Chasing AI Citations](https://www.youtube.com/watch?v=QPm1GA_5CZA), 28.04.2026).
- **My call:** I side closer to Schwartz on execution risk but don't reject Reddit outright. The difference between the two isn't really about whether Reddit matters — both agree it does — it's about *how* you show up. Simmonds' own playbook already builds in the caution Schwartz is warning about (named individual accounts, no links in the first five days, mod outreach before posting). The risk case is really against fast, faceless, link-first brand behavior, not against Reddit participation itself. I'd follow Simmonds' structure but budget for it as a slow relationship-building channel, not a fast-turnaround distribution channel.

### Disagreement 2: Is "AI SEO" a genuinely new discipline, or repackaged SEO fundamentals?

- **Britney Muller** argues GEO is mostly rediscovery: LLM citation behavior largely mirrors underlying search-engine ranking factors already understood in traditional SEO — fresh, well-ranking content gets cited; spammy listicles that rank also get cited (source: Britney Muller, [LinkedIn post](https://www.linkedin.com/in/britneymuller/), 2025).
- **Mike King** argues the opposite: that this moment needs "a wholesale rethink," not incremental adaptation, because the underlying retrieval mechanisms (relevance scoring across multiple platforms, interaction signals, passage-level retrieval) are different enough from classic ranking that treating it as "just SEO" undersells what's changed (source: Mike King, [Relevance Engineering interview](https://www.youtube.com/watch?v=pQLivtcqCZs), 27.05.2025).
- **My call:** I lean toward Muller here, with a caveat. The fundamentals-first view is the safer default for a resource-constrained team — chasing platform-specific tricks is a worse use of limited time than getting E-E-A-T, crawlability, and content quality right, which is advice virtually every source in this research converges on regardless of which "side" they're on. But King's point about passage-level retrieval and multi-platform interplay is a real structural difference this playbook incorporates directly (Step 2), so it's not pure fundamentals-only. I'd frame it as: 90% fundamentals, 10% genuinely new structural work.

### Disagreement 3: Whether scaling AI-generated content is a viable strategy

- **Ross Simmonds** cites CNET's AI-content experiment as evidence scaling works: despite the public backlash and factual-error controversy, the AI-written content generated millions of visits, ~2,400 backlinks, and roughly $1.3M in equivalent organic traffic value before CNET pulled it (source: Ross Simmonds, cited above).
- **Glenn Gabe's** case-study tracking across core updates shows the other side of the same story: sites that scaled low-quality AI content saw an initial traffic spike, then a sharp drop once a core update specifically targeted that pattern — the "Mt. AI" phenomenon (source: Glenn Gabe, cited above).
- **My call:** These aren't actually contradictory once you line up the timeframes — Simmonds is describing what happened *before* the reckoning, Gabe is describing the reckoning. I take Gabe's side for anything durable: the CNET numbers are a snapshot from before Google's countermeasures caught up, and CNET itself shut the experiment down. Scaled AI content without human review is a short-term arbitrage, not a strategy — which is also why it's the first thing this playbook explicitly rejects (see Part 3).

---

## Part 3 — What I rejected and why

1. **Prompt-injection tactics (hidden white-text instructions telling an AI to recommend your brand).** Garrett Sussman raises this as a real tactic people are trying, and I'm not including it. Beyond the fact that it's the kind of manipulation LLM providers actively patch against, it's a trust-destroying tactic to build a durable content function around — even Sussman, who describes it neutrally as something people are doing, doesn't call it sustainable (source: Garrett Sussman, cited above). A playbook that recommends this has an expiration date built in.

2. **PBN-style link building adapted for AI citation ("buy authority to get cited").** This showed up as a tempting shortcut in the research, but Garrett Sussman himself waves it off in favor of building genuinely link-worthy assets, and Lily Ray's independent analysis of Google's crackdown pattern on "too much SEO" content reinforces that manufactured authority signals are exactly the kind of thing search engines have gotten progressively better at detecting over successive core updates (source: Garrett Sussman, cited above; Lily Ray, cited above). I left it out entirely rather than softening it into a caveat — it doesn't belong in a "sustainable production" SOP at all.

3. **Chasing every AI platform's individual optimization quirks (AI Mode vs. AI Overviews vs. Perplexity vs. ChatGPT each treated as a separate workstream).** Kevin Indig's data shows AI Mode and AI Overviews genuinely require different approaches (source: cited above), which is real and worth knowing — but building separate production workflows per platform is a resourcing trap for a small team. I folded platform awareness into Step 1 (research) rather than turning it into parallel production tracks, because none of the sources actually demonstrated that platform-specific production (versus platform-aware research) changes outcomes enough to justify the overhead.

---

## Part 4 — My original ideas

**The "Citation Debt Ledger."**

None of the ten sources proposed this specific workflow, though several (Simmonds on dark mentions, Indig on the 1% AI Overview click rate) independently describe the same underlying problem: most AI-driven brand visibility is now invisible to standard analytics, so a content team has no reliable way to tell if a given piece of content is actually working inside AI answers.

My idea: instead of treating this as an unsolvable measurement gap, build a lightweight recurring manual audit into the production calendar itself. Once a month, take a fixed panel of 15–20 realistic buyer questions for your product category, run them against ChatGPT, Perplexity, Gemini, and Google AI Mode, and log whether/how the brand is mentioned — cited with a link, mentioned without a link, or absent — in a simple spreadsheet. Do this *before and after* each significant content push, so you have a rough before/after comparison tied to specific publishing dates, even without perfect attribution.

This wouldn't be rigorous causal measurement — a lot could shift the answer besides your content (model updates, seasonality, a competitor's push). But it converts an invisible metric into a directionally useful one at near-zero cost, which is exactly the gap the sources describe and don't solve for. It's a poor-man's version of what tools like Profound or Peec do commercially, sized for a team that can't yet justify that spend. I think it works because the actual bottleneck isn't sophistication — it's that most teams currently track *nothing* in this category, so even an imperfect manual signal is a real improvement over flying blind.

---

## Part 5 — Weaknesses of this playbook

- **Source pool has a self-selection bias.** All ten experts are agency owners, consultants, or authors of paid frameworks/tools (iPullRank's AI Search Manual, Aleyda Solis's Orainti frameworks, Cyrus Shepard's Zyppy). Several recommendations converge suspiciously well with tools or services those same people sell. I didn't independently verify any of the underlying data (Cyrus Shepard's "23 factors," Kevin Indig's clickstream study, the CNET traffic figures) — I'm relying on their self-reported analysis. This is an evidence-quality gap, not just a bias-awareness footnote.

- **Everything here is untested by me.** This is a synthesis of what practitioners say works, not a validated result from running it. AgriFuture-style B2B/export businesses and the SaaS companies most of these sources are talking about have very different buyer journeys, content formats, and query patterns — a lot of this may need real adaptation, not direct application, outside a SaaS/tech B2B context.

- **The research is US/English-market heavy.** Nearly all sources discuss English-language, US-centric search and LLM behavior (Google AI Overviews, ChatGPT, Reddit's US-heavy user base). None of the sources speak to how this plays out in non-English markets, regional search engines, or WhatsApp/messaging-first buyer behavior — a real gap if this playbook needs to generalize beyond a US/English context.

- **The correlational-evidence sections are the shakiest.** Cyrus Shepard explicitly caveats his own 23-factor ranking as "correlations from evidence, not a confirmed ranking formula" — and I've built structural recommendations (Step 2) partly on top of that. If the underlying correlation is wrong or platform-specific, this playbook's structural guidance could be wrong too.

- **This entire landscape is moving fast enough that parts of this may already be stale.** The sources span May 2025 to May 2026, and several of them (Mike King on Google's guide, Lily Ray on GEO spam crackdowns) are explicitly describing things that changed mid-research. A six-month-old recommendation in this space carries real decay risk — this needs a re-audit cadence, not a one-time write-up.

- **The three "expert disagreements" I resolved were resolved by my judgment, not by additional evidence.** I didn't run experiments to break the ties — I made a reasoned call in each case, but a different reasonable person reading the same ten sources could land differently, particularly on the Reddit-risk question.
