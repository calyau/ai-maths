---
concept: Convexity Lemma for Square Sums
slug: convexity-lemma
category: regularity-method
subcategory: technical-lemmas
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Extremal Problems"
chapter_number: 4
pdf_page: 110
section: "IV.5 Szemerédi's Regularity Lemma"
extraction_confidence: high
aliases:
  - "Lemma 27"
prerequisites: []
extends: []
related:
  - square-mean
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "How does the convexity lemma support the regularity proof?"
---

# Quick Definition
If a subset of numbers with average $d$ deviates from the overall average $D$ by $\delta$, then the average of squares increases by at least $\gamma\delta^2$ (where $\gamma$ is the fraction of the subset).

# Core Definition
**Lemma 27**: Let $(d_i)_{i=1}^s \subset \mathbb{R}$, $1 \le t < s$, $D = \frac{1}{s}\sum d_i$, $d = \frac{1}{t}\sum_{i=1}^t d_i$. Then $\frac{1}{s}\sum d_i^2 \ge D^2 + \frac{t}{s}(D-d)^2$. In particular, if $t \ge \gamma s$ and $|D-d| \ge \delta$, then $\frac{1}{s}\sum d_i^2 \ge D^2 + \gamma\delta^2$ (Bollobás, p. 141).

# Prerequisites
This is a mathematical lemma with no graph-theoretic prerequisites.

# Key Properties
1. Based on convexity of $x^2$
2. Quantifies how much the sum of squares exceeds the square of the mean
3. Applied to densities in the regularity lemma proof

# Context & Application
Used in Lemma 28 to show that non-uniform pairs increase the square mean $q(\mathcal{P})$.

# Examples
**Example** (pp. 141-142): Applied with $d_i = d(D_{iu}, D_{jv})$ for density values within a non-uniform pair, showing the square mean increases.

# Relationships
## Enables
- **regularity-refinement-lemma** — Lemma 28 uses this

# Source Reference
Chapter IV, Section IV.5, page 141. Lemma 27.

# Verification Notes
- Definition source: Direct from p. 141
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
