---
concept: Unitary Representation
slug: unitary-representation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.3 Unitary Representations"
extraction_confidence: high
aliases: []
prerequisites: [group-representation, hermitian-form]
extends: [group-representation]
related: [maschkes-theorem, g-invariant-hermitian-form]
contrasts_with: []
answers_questions: ["What is a unitary representation?"]
---
# Quick Definition
A representation rho: G -> GL(V) on a Hermitian space V is unitary if every rho_g preserves the Hermitian form: (gv, gw) = (v, w). Every representation of a finite group can be made unitary by choosing an appropriate G-invariant Hermitian form.
# Core Definition
A representation rho on a Hermitian space V is unitary if rho_g is a unitary operator for every g: (gv, gw) = (v, w) (Artin, (10.3.2), p. 306). A matrix representation R is unitary if R_g is unitary for every g, i.e., R: G -> U_n (10.3.3). Theorem 10.3.6: For any representation of a finite group, there exists a G-invariant positive definite Hermitian form. The averaged form (v, w) = (1/|G|) sum_g {gv, gw} does the job (10.3.7).
# Prerequisites
- **Group representation** — Unitary is a property of representations
- **Hermitian form** — The form that is preserved
# Key Properties
1. (gv, gw) = (v, w) for all g, v, w
2. If W is G-invariant, W^perp is also G-invariant (Lemma 10.3.4)
3. Every unitary representation decomposes as orthogonal sum of irreducibles (Corollary 10.3.5)
4. Every representation of a finite group can be made unitary (Theorem 10.3.6)
5. Every finite subgroup of GL_n is conjugate to a subgroup of U_n (Corollary 10.3.8(d))
# Context & Application
The ability to make any representation unitary (via averaging) is the key to Maschke's theorem. It is a distinctive feature of finite groups. The averaging technique appears repeatedly in representation theory.
# Examples
**Example 1** (p. 308): The permutation matrices in the representation N of S_3 on C^3 are unitary (in fact orthogonal).
# Relationships
## Builds Upon
- **Group representation** — Unitarity is a property of representations
## Enables
- **Maschke's theorem** — Proved via unitary representations
# Source Reference
Chapter 10: Group Representations, Section 10.3, pages 306-308.
# Verification Notes
- Definition source: Direct from (10.3.2)
- Confidence rationale: Explicitly defined with key theorem
- Uncertainties: None
- Cross-reference status: Verified
