---
concept: Density Approximation Lemma
slug: density-lemma
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
  - "Lemma 26"
prerequisites:
  - edge-density
extends: []
related:
  - szemeredis-regularity-lemma
contrasts_with: []
answers_questions:
  - "How does density change when restricting to large subsets?"
---

# Quick Definition
If $X^* \subset X$ with $|X^*| \ge (1-\gamma)|X|$ and $Y^* \subset Y$ with $|Y^*| \ge (1-\delta)|Y|$, then $|d(X^*,Y^*) - d(X,Y)| < \gamma + \delta$.

# Core Definition
**Lemma 26**: If $|X^*| \ge (1-\gamma)|X|$ and $|Y^*| \ge (1-\delta)|Y|$, then $|d(X^*,Y^*) - d(X,Y)| < \gamma + \delta$ and $|d^2(X^*,Y^*) - d^2(X,Y)| < 2(\gamma + \delta)$ (Bollobás, pp. 140-141).

# Prerequisites
- **Edge density** — The quantity being bounded

# Key Properties
1. Density is approximately preserved under small subset removal
2. Works by bounding $e(X,Y) - e(X^*,Y^*)$ from both sides
3. Used repeatedly in the proof of Lemma 28

# Context & Application
This technical lemma ensures that the density calculations in the regularity lemma proof remain stable under small perturbations.

# Examples
**Example** (pp. 140-141): The complement argument: replacing $G$ by $\overline{G}$ swaps $d$ and $1-d$, giving the other inequality direction.

# Relationships
## Enables
- **szemeredis-regularity-lemma** — Used in the proof

# Source Reference
Chapter IV, Section IV.5, pages 140-141. Lemma 26.

# Verification Notes
- Definition source: Direct from pp. 140-141
- Confidence rationale: Explicitly stated with proof
- Uncertainties: None
- Cross-reference status: Verified
