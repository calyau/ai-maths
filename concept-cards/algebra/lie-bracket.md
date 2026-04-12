---
concept: Lie Bracket
slug: lie-bracket
category: linear-groups
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Groups"
chapter_number: 9
pdf_page: 264
section: "9.6 The Lie Algebra"
extraction_confidence: high
aliases: ["commutator bracket", "bracket operation"]
prerequisites: [lie-algebra]
extends: []
related: []
contrasts_with: []
answers_questions: ["What is the Lie bracket?"]
---
# Quick Definition
The Lie bracket is the operation [A, B] = AB - BA on matrices. It is the fundamental algebraic operation on a Lie algebra, satisfying bilinearity, skew symmetry, and the Jacobi identity.
# Core Definition
The bracket is defined by [A, B] = AB - BA (Artin, p. 286). It is zero if and only if A and B commute. It satisfies: bilinearity, skew symmetry [v, w] = -[w, v], and the Jacobi identity [A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0 (9.6.5, 9.6.6). The bracket is closed on each Lie algebra (e.g., [skew-symmetric, skew-symmetric] = skew-symmetric).
# Prerequisites
- **Lie algebra** — The bracket is the algebraic structure on Lie algebras
# Key Properties
1. [A, B] = AB - BA
2. [A, B] = 0 iff A and B commute
3. Bilinear in both arguments
4. Skew-symmetric: [A, B] = -[B, A]
5. Jacobi identity: [A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0
6. NOT associative in general
7. Closed on each classical Lie algebra
# Context & Application
The bracket is the infinitesimal version of the group commutator. It measures the failure of commutativity in the Lie algebra and hence (locally) in the group.
# Examples
**Example 1** (p. 286): For skew-symmetric A, B: [A, B]^t = (AB)^t - (BA)^t = B^t A^t - A^t B^t = (-B)(-A) - (-A)(-B) = BA - AB = -[A, B], so [A, B] is skew-symmetric.
# Relationships
## Builds Upon
- **Lie algebra** — The bracket is defined on Lie algebras
# Common Errors
- **Error**: Assuming the bracket is associative
  **Correction**: The bracket satisfies the Jacobi identity, not associativity
# Source Reference
Chapter 9: Linear Groups, Section 9.6, pages 286-287.
# Verification Notes
- Definition source: Direct from p. 286
- Confidence rationale: Explicitly defined with axioms
- Uncertainties: None
- Cross-reference status: Verified
