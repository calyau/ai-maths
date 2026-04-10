---
concept: Canonical Colouring
slug: canonical-colouring
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 194
section: "VI.2 Canonical Ramsey Theorems"
extraction_confidence: high
aliases:
  - "S-canonical colouring"
  - "c_S"
prerequisites:
  - ramsey-theorem-infinite
extends: []
related:
  - canonical-ramsey-theorem
contrasts_with: []
answers_questions:
  - "What is a canonical colouring?"
---

# Quick Definition
An S-canonical colouring c_S: N⁽ʳ⁾ → N⁽ˢ⁾ (for S ⊂ [r], |S| = s) assigns each r-set its projection to the coordinates in S. Two r-sets get the same colour iff they agree on their ith elements for all i ∈ S.

# Core Definition
Given N ⊂ ℕ, α = {a₁,...,aᵣ} ∈ N⁽ʳ⁾ (a₁ < ... < aᵣ), and S ⊂ [r], the **S-canonical colouring** c_S: N⁽ʳ⁾ → N⁽ˢ⁾ is defined by c_S(α) = α_S = {aᵢ : i ∈ S}. Two r-sets get the same colour iff their ith elements coincide for i ∈ S. Special cases: c_∅ is monochromatic, c_{[r]} is all-distinct (Bollobás, p. 194).

# Prerequisites
- **Ramsey theorem (infinite)** — context for canonical colourings

# Key Properties
1. There are exactly 2ʳ canonical colourings (one per S ⊂ [r])
2. c_∅ = monochromatic colouring (one colour)
3. c_{[r]} = all-distinct colouring
4. For r = 2: c_∅ (all same), c_{1} (first determines), c_{2} (second determines), c_{1,2} (all different)
5. Every canonical colouring is irreducible

# Relationships
## Enables
- **Canonical Ramsey theorem** — every colouring reduces to a canonical one on some infinite subset

# Source Reference
Chapter VI: Ramsey Theory, Section VI.2, pages 194–195.

# Verification Notes
- Definition source: Direct from p. 194
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
