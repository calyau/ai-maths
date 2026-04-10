---
concept: Szemerédi's Theorem
slug: szemeredis-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 215
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Erdős-Turán conjecture (proved)"
  - "density version of van der Waerden"
prerequisites:
  - van-der-waerden-theorem
extends:
  - van-der-waerden-theorem
related:
  - regularity-lemma
contrasts_with: []
answers_questions:
  - "Does every dense set of integers contain arithmetic progressions?"
---

# Quick Definition
Every set of natural numbers with positive upper density contains arbitrarily long arithmetic progressions. This is a far-reaching strengthening of van der Waerden's theorem — density suffices, no colouring needed.

# Core Definition
**Szemerédi's theorem** (Bollobás, p. 215): If A ⊂ ℕ satisfies lim sup |A ∩ [N]|/N > 0, then A contains arbitrarily long arithmetic progressions. By compactness, for every δ > 0 and p ≥ 1, there exists N such that every subset of [N] with ≥ δN elements contains a p-term AP.

This was conjectured by Erdős and Turán in the 1930s. The case p = 3 was proved by Roth (1953). The full theorem was proved by Szemerédi (1975) using his regularity lemma, and reproved by Fürstenberg (1977) using ergodic theory.

# Prerequisites
- **Van der Waerden's theorem** — Szemerédi's theorem implies it

# Key Properties
1. Positive upper density suffices for arbitrarily long APs
2. Implies van der Waerden's theorem (largest colour class has positive density)
3. Szemerédi's proof used the regularity lemma
4. Fürstenberg's proof used ergodic theory
5. Both the proof and the theorem revolutionized combinatorics and ergodic theory

# Context & Application
Szemerédi's theorem is one of the most influential results in combinatorics. Its proof (via the regularity lemma) revolutionized extremal graph theory, and Fürstenberg's ergodic-theoretic proof revitalized ergodic theory.

# Relationships
## Builds Upon
- **Van der Waerden's theorem** — density version

## Related
- **Regularity lemma** — needed in Szemerédi's original proof (Ch IV.5)

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, pages 215–216.

# Verification Notes
- Definition source: Direct from pp. 215–216
- Confidence rationale: Explicitly discussed (proof not given)
- Uncertainties: None
- Cross-reference status: Verified
