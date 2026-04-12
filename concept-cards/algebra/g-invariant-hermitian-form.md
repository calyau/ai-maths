---
concept: G-Invariant Hermitian Form
slug: g-invariant-hermitian-form
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
aliases: ["G-invariant form"]
prerequisites: [hermitian-form, group-representation]
extends: []
related: [unitary-representation, maschkes-theorem]
contrasts_with: []
answers_questions: ["How is a G-invariant Hermitian form constructed?"]
---
# Quick Definition
A positive definite Hermitian form (v, w) on V is G-invariant if (gv, gw) = (v, w) for all g in G. For any finite group representation, such a form exists and can be constructed by averaging any positive definite form over the group.
# Core Definition
A positive definite Hermitian form on V is G-invariant if (gv, gw) = (v, w) for all g, v, w (Artin, p. 307). Theorem 10.3.6: For any representation of a finite group, a G-invariant positive definite Hermitian form exists. Construction: start with any positive definite Hermitian form {,} and average: (v, w) = (1/|G|) sum_g {gv, gw} (10.3.7).
# Prerequisites
- **Hermitian form** — The type of form being averaged
- **Group representation** — The representation determines the averaging
# Key Properties
1. Constructed by averaging: (v, w) = (1/|G|) sum_g {gv, gw}
2. The averaged form is automatically Hermitian, positive definite, and G-invariant
3. G-invariance is proved using the reindexing trick (right multiplication by h)
4. Makes the representation unitary
5. Enables orthogonal complement decomposition of G-invariant subspaces
# Context & Application
This construction is the key to Maschke's theorem. By making any representation unitary, we ensure that orthogonal complements of G-invariant subspaces are also G-invariant, enabling the inductive decomposition into irreducibles.
# Examples
**Example 1** (p. 307): Starting with the standard Hermitian form X*Y on C^n and averaging over G produces a G-invariant form.
# Relationships
## Enables
- **Unitary representation** — The representation becomes unitary with respect to the averaged form
- **Maschke's theorem** — Proved via G-invariant forms
# Source Reference
Chapter 10: Group Representations, Section 10.3, Theorem 10.3.6, pages 307-308.
# Verification Notes
- Definition source: Direct from (10.3.7) and Theorem 10.3.6
- Confidence rationale: Explicitly defined with construction
- Uncertainties: None
- Cross-reference status: Verified
