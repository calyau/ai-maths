---
concept: Erdős-Rado Canonical Ramsey Theorem
slug: canonical-ramsey-theorem
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
  - "Theorem VI.9"
  - "Erdős-Rado theorem"
  - "canonical colouring theorem"
prerequisites:
  - ramsey-theorem-infinite
  - canonical-colouring
extends:
  - ramsey-theorem-infinite
related:
  - canonical-colouring
contrasts_with: []
answers_questions:
  - "What happens with infinitely many colours in Ramsey's theorem?"
---

# Quick Definition
For every colouring c: ℕ⁽ʳ⁾ → ℕ (with any number of colours), there is an infinite subset M of ℕ such that c restricted to M⁽ʳ⁾ is canonical — equivalent to one of 2ʳ specific standard colourings.

# Core Definition
**Theorem 9** (Bollobás, p. 196): Let r be a positive integer and c: ℕ⁽ʳ⁾ → ℕ a colouring. Then there is an infinite subset M of ℕ such that the restriction of c to M⁽ʳ⁾ is canonical.

For r = 2 (Theorem 8): any colouring of ℕ⁽²⁾ with arbitrarily many colours has an infinite subset where the colouring is one of: monochromatic (c_∅), all-distinct (c_{1,2}), first-vertex-determines (c_{1}), or second-vertex-determines (c_{2}).

# Prerequisites
- **Ramsey theorem (infinite)** — used in the proof
- **Canonical colouring** — the target colourings

# Key Properties
1. Works for any number of colours (even infinitely many)
2. There are exactly 2ʳ canonical colourings of ℕ⁽ʳ⁾ (one per subset S ⊂ [r])
3. Strictly stronger than the infinite Ramsey theorem (which handles only finitely many colours)
4. For finite colours, the only canonical colouring is monochromatic (c_∅)

# Context & Application
The Erdős-Rado canonical theorem (1950) extends Ramsey's theorem to infinitely many colours. It shows that despite having unlimited colours available, the structure on an infinite subset must be one of finitely many canonical types.

# Examples
**Example** (p. 195): For r = 2, the four canonical colourings are: (1) all same colour, (2) all different, (3) colour depends on smaller element, (4) colour depends on larger element.

# Relationships
## Builds Upon
- **Ramsey theorem (infinite)** — extends to infinitely many colours

## Related
- **Canonical colouring** — the standard forms

# Source Reference
Chapter VI: Ramsey Theory, Section VI.2, Theorems 8–9, pages 194–197.

# Verification Notes
- Definition source: Direct theorem statements
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
