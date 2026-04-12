---
concept: One-Dimensional Character
slug: one-dimensional-character
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.5 One-Dimensional Characters"
extraction_confidence: high
aliases: ["linear character"]
prerequisites: [character-of-a-representation]
extends: [character-of-a-representation]
related: [trivial-representation]
contrasts_with: []
answers_questions: ["What is a one-dimensional character?"]
---
# Quick Definition
A one-dimensional character is a homomorphism chi: G -> C*. It is simultaneously a representation, a character, and a group homomorphism. For abelian groups, ALL irreducible characters are one-dimensional.
# Core Definition
A one-dimensional character is the character of a representation on a one-dimensional vector space. Since rho_g is a 1x1 matrix, chi(g) = rho_g = R_g, and chi is a homomorphism from G to C* (Artin, p. 315). Every commutator is in the kernel. For a finite abelian group, every irreducible character is one-dimensional and the number of irreducible characters equals |G| (Theorem 10.5.2).
# Prerequisites
- **Character of a representation** — A one-dimensional character is a special case
# Key Properties
1. chi is a homomorphism from G to C*
2. chi(g) is a root of unity when g has finite order
3. Commutators are in ker(chi), so chi factors through G/[G,G]
4. Kernels of one-dimensional characters reveal normal subgroups
5. For abelian groups: all irreducibles are 1D, count = |G|
# Context & Application
One-dimensional characters are the simplest representations and the starting point for building character tables. Normal subgroups can be read off as kernels of one-dimensional characters.
# Examples
**Example 1** (p. 315): The character table of C_3 = {1, x, x^2}: chi_1 = (1,1,1), chi_2 = (1, omega, omega^2), chi_3 = (1, omega^2, omega) where omega = e^{2pi i/3}.
**Example 2** (p. 315): The kernel of chi_2 in the tetrahedral group's character table is C(1) union C(y), a normal subgroup of order 4.
# Relationships
## Builds Upon
- **Character of a representation** — Special case of dimension 1
## Related
- **Trivial representation** — The simplest one-dimensional character (all 1's)
# Common Errors
- **Error**: Assuming higher-dimensional characters are homomorphisms
  **Correction**: Only one-dimensional characters are homomorphisms; higher-dimensional characters are sums of roots of unity (Warning, p. 316)
# Source Reference
Chapter 10: Group Representations, Section 10.5, pages 315-316.
# Verification Notes
- Definition source: Direct from p. 315
- Confidence rationale: Explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
