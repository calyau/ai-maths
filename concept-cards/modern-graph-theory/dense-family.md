---
concept: Dense and Thin Families
slug: dense-family
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 218
section: "VI.5 Subsequences"
extraction_confidence: high
aliases:
  - "dense family"
  - "thin family"
prerequisites:
  - galvin-prikry-theorem
extends: []
related:
  - hindmans-theorem
contrasts_with: []
answers_questions:
  - "What is a dense family of finite sets?"
  - "What is a thin family of finite sets?"
---

# Quick Definition
A family G ⊂ ℕ^(<ω) is dense if G ∩ M^(<ω) ≠ ∅ for every infinite M. It is thin if no member is an initial segment of another. These notions enable powerful corollaries of the Galvin-Prikry theorem.

# Core Definition
A family G ⊂ ℕ^(<ω) (finite subsets of ℕ) is **dense** if G ∩ M^(<ω) ≠ ∅ for every M ∈ ℕ^(ω). It is **thin** if no member is an initial segment of another (X < Y implies X ∉ G or X ∪ Y ∉ G). For example, ℕ^(r) is thin for each r. **Corollary 31**: if G is thin and k-coloured, some infinite A has all members of G in A monochromatic (Bollobás, p. 218).

# Prerequisites
- **Galvin-Prikry theorem** — dense/thin families are used in its corollaries

# Key Properties
1. Dense: every infinite set contains a member of G
2. Thin: no element is an initial segment of another
3. Corollary 30: if G is dense, there exists M with every A ⊂ M having an initial segment in G
4. Corollary 31: thin families satisfy Ramsey property for finite colourings

# Relationships
## Related
- **Hindman's theorem** — applications of these concepts

# Source Reference
Chapter VI: Ramsey Theory, Section VI.5, Corollaries 30–31, page 218.

# Verification Notes
- Definition source: Direct from p. 218
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
