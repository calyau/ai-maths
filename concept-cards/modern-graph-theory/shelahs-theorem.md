---
concept: Shelah's Theorem
slug: shelahs-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 210
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.26"
  - "Shelah's extension of Hales-Jewett"
  - "Shelah's bounds"
prerequisites:
  - hales-jewett-theorem
  - shelahs-pigeon-hole-principle
extends:
  - hales-jewett-theorem
related:
  - van-der-waerden-theorem
contrasts_with: []
answers_questions:
  - "What are the best known bounds for the Hales-Jewett function?"
---

# Quick Definition
Shelah gave the first primitive recursive upper bound for the Hales-Jewett function: HJ(p+1,k) ≤ n·S(n, k^{(p+1)^n}) where n = HJ(p,k). This implies W(p,k) grows at most like f₄ (the fourth Ackermann level).

# Core Definition
**Theorem 26** (Bollobás, p. 210): Given integers p and k, there is a minimal integer n = HJ(p,k) such that every k-colouring [p]ⁿ → [k] contains a monochromatic line. Furthermore, HJ(p+1,k) ≤ n·S(n, k^{(p+1)^n}).

Shelah's breakthrough (1988) was proving this primitive recursive bound, replacing the Ackermann-function bounds from earlier proofs. The proof uses Shelah's pigeon-hole principle (Lemma 24) and a "telescoping" argument with s-extensions.

# Prerequisites
- **Hales-Jewett theorem** — Shelah gives effective bounds
- **Shelah's pigeon-hole principle** — key lemma in the proof

# Key Properties
1. HJ(p,k) has primitive recursive bounds
2. W(p,k) ≤ p^{HJ(p,k)} (still the best known bound)
3. The bound involves the Shelah function S(n,k) with S(1,k) = k+1, S(n+1,k) ≤ k^{S(n,k)^{2n}} + 1
4. Growth is like f₄ (tower of towers), still enormous but primitive recursive

# Context & Application
Shelah's theorem (1988) was a remarkable breakthrough, coming over 60 years after van der Waerden's original proof. It showed that the incredibly fast growth of the original bounds was an artifact of the proof, not the theorem.

# Relationships
## Builds Upon
- **Hales-Jewett theorem** — provides effective bounds

## Related
- **Van der Waerden's theorem** — best known bounds come from Shelah

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 26, pages 210–213.

# Verification Notes
- Definition source: Direct theorem statement from p. 210
- Confidence rationale: Explicit theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
