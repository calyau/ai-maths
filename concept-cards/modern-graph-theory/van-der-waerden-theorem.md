---
concept: Van der Waerden's Theorem
slug: van-der-waerden-theorem
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 207
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.22"
  - "van der Waerden function"
  - "W(p)"
  - "W(p,k)"
prerequisites:
  - ramsey-number
extends: []
related:
  - hales-jewett-theorem
  - szemeredis-theorem
  - schurs-theorem
  - rados-theorem
contrasts_with: []
answers_questions:
  - "What is van der Waerden's theorem?"
---

# Quick Definition
Given p and k, if n is large enough, every k-colouring of [n] contains a monochromatic arithmetic progression of length p. The van der Waerden function W(p,k) gives the minimal such n.

# Core Definition
**Theorem 22** (Bollobás, p. 207): Given p and k, if n is large enough, then every k-colouring of [n] contains a monochromatic arithmetic progression of length p. The van der Waerden function W(p) = W(p,2), and W(p,k) is the minimal n. Known values: W(3) = 9, W(4) = 35, W(5) = 178.

Van der Waerden's theorem (1927) predates Ramsey's theorem and is deduced from the Hales-Jewett theorem in the text.

# Prerequisites
- **Ramsey number** — van der Waerden's theorem is a Ramsey-type result

# Key Properties
1. W(p,k) is always finite
2. W(3) = 9, W(4) = 35, W(5) = 178
3. Original proof gave Ackermann-function growth
4. Shelah's theorem gives primitive recursive bound: W(p,k) ≤ p^{HJ(p,k)}
5. Best known bounds still grow extremely fast

# Context & Application
Van der Waerden's theorem (1927) is perhaps the first deep result of Ramsey theory. It states that monochromatic arithmetic progressions are unavoidable in any finite colouring of the integers.

# Examples
**Example** (p. 207): W(3) = 9: every 2-colouring of [9] contains a monochromatic 3-term AP.

# Relationships
## Related
- **Hales-Jewett theorem** — implies van der Waerden's theorem
- **Szemerédi's theorem** — density version: every dense set contains long APs
- **Rado's theorem** — van der Waerden is essentially a special case

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 22, pages 207–208.

# Verification Notes
- Definition source: Direct theorem statement from p. 207
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
