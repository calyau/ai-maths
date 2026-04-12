---
concept: Representations of Abelian Groups
slug: abelian-group-representations
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
aliases: []
prerequisites: [one-dimensional-character, irreducible-representation]
extends: []
related: []
contrasts_with: []
answers_questions: ["What are the representations of abelian groups?"]
---
# Quick Definition
For a finite abelian group of order N, every irreducible representation is one-dimensional, there are exactly N irreducible representations, and every matrix representation is simultaneously diagonalizable.
# Core Definition
Theorem 10.5.2: Let G be a finite abelian group. (a) Every irreducible character is one-dimensional, and the number of irreducible characters equals |G|. (b) Every matrix representation R of G is simultaneously diagonalizable: there exists P such that P^{-1} R_g P is diagonal for all g (Artin, p. 316).
# Prerequisites
- **One-dimensional character** — All irreducibles of abelian groups are 1D
- **Irreducible representation** — The building blocks
# Key Properties
1. All irreducibles are one-dimensional
2. Number of irreducibles = |G|
3. |G| = 1^2 + ... + 1^2 = N (all dimensions are 1)
4. Every representation is simultaneously diagonalizable
5. Every conjugacy class is a single element
# Examples
**Example 1** (p. 316): C_3 has three irreducible characters: chi_k(x) = omega^k for k = 0, 1, 2 where omega = e^{2pi i/3}.
# Relationships
## Builds Upon
- **One-dimensional character** — All irreducibles are 1D for abelian groups
# Source Reference
Chapter 10: Group Representations, Section 10.5, Theorem 10.5.2, page 316.
# Verification Notes
- Definition source: Direct from Theorem 10.5.2
- Confidence rationale: Explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
