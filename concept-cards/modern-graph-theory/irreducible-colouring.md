---
concept: Irreducible Colouring
slug: irreducible-colouring
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 194
section: "VI.2 Canonical Ramsey Theorems"
extraction_confidence: high
aliases:
  - "unavoidable colouring"
prerequisites:
  - canonical-colouring
extends: []
related:
  - canonical-ramsey-theorem
contrasts_with: []
answers_questions:
  - "What is an irreducible colouring?"
---

# Quick Definition
A colouring c: N⁽ʳ⁾ → C is irreducible if for every infinite N₁ ⊂ N, the restriction of c to N₁⁽ʳ⁾ is equivalent to c. The 2ʳ canonical colourings are exactly the irreducible colourings.

# Core Definition
A colouring c: N⁽ʳ⁾ → C is **irreducible** if for every infinite subset N₁ of N, the restriction of c to N₁⁽ʳ⁾ is equivalent to c. A set C of colourings is **unavoidable** if for every colouring c of N⁽ʳ⁾ there is an infinite M ⊂ N such that the restriction to M⁽ʳ⁾ is equivalent to a member of C. Erdős and Rado proved that for every r there is a finite unavoidable family of irreducible colourings — namely, the 2ʳ canonical colourings (Bollobás, p. 194).

# Prerequisites
- **Canonical colouring** — the canonical colourings are the irreducible ones

# Key Properties
1. There are exactly 2ʳ irreducible colourings of ℕ⁽ʳ⁾
2. They are the S-canonical colourings for S ⊂ [r]
3. The set of canonical colourings is unavoidable

# Relationships
## Related
- **Canonical Ramsey theorem** — proves the canonical colourings form an unavoidable set

# Source Reference
Chapter VI: Ramsey Theory, Section VI.2, page 194.

# Verification Notes
- Definition source: Direct from p. 194
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
