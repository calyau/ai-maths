---
concept: Symplectic Group
slug: symplectic-group
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.1 The Classical Groups"
extraction_confidence: high
aliases: ["Sp_{2n}"]
prerequisites: [symplectic-form]
extends: [general-linear-group]
related: [classical-groups]
contrasts_with: [orthogonal-group]
answers_questions: ["What is the symplectic group?"]
---
# Quick Definition
The symplectic group Sp_{2n} is the group of real 2n x 2n matrices P preserving the standard skew-symmetric form X^t S Y, where S = [[0, I],[-I, 0]].
# Core Definition
Sp_{2n} = {P in GL_{2n}(R) | P^t S P = S} where S = [[0, I],[-I, 0]] (Artin, (9.1.4), p. 264). Though not obvious from the definition, symplectic matrices have determinant 1 (p. 265).
# Prerequisites
- **Symplectic form** — Sp_{2n} preserves the standard symplectic form
# Key Properties
1. P^t S P = S where S = [[0, I],[-I, 0]]
2. All symplectic matrices have determinant 1
3. Sp_2 = SL_2 (in dimension 2, symplectic = special linear)
# Construction / Recognition
## To Recognize:
1. Check P^t S P = S where S is the standard symplectic matrix
# Context & Application
The symplectic group arises in Hamiltonian mechanics (canonical transformations) and symplectic geometry. In quantum mechanics, metaplectic representations (a double cover of Sp) play an important role.
# Examples
**Example 1** (p. 264): Sp_2 = SL_2(R) — the 2x2 case coincides with the special linear group.
# Relationships
## Builds Upon
- **Symplectic form** — Sp_{2n} preserves this form
## Contrasts With
- **Orthogonal group** — Preserves a symmetric form, not a skew-symmetric one
# Common Errors
- **Error**: Defining Sp_{2n} with dimension 2n+1
  **Correction**: Symplectic groups only exist in even dimensions
# Common Confusions
- **Confusion**: Thinking symplectic matrices can have det != 1
  **Clarification**: All symplectic matrices automatically have determinant 1
# Source Reference
Chapter 9: Linear Groups, Section 9.1, page 264.
# Verification Notes
- Definition source: Direct from (9.1.4)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
