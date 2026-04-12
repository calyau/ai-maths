---
concept: G-Invariant Linear Transformation
slug: g-invariant-linear-transformation
category: group-representations
subcategory: null
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Group Representations"
chapter_number: 10
pdf_page: 301
section: "10.7 Schur's Lemma"
extraction_confidence: high
aliases: ["intertwining operator", "G-equivariant map"]
prerequisites: [group-representation]
extends: []
related: [schurs-lemma]
contrasts_with: []
answers_questions: ["What is a G-invariant linear transformation?"]
---
# Quick Definition
A linear transformation T: V' -> V is G-invariant (with respect to representations rho, rho') if T(gv') = gT(v') for all g and v'. Schur's Lemma characterizes these maps between irreducible representations.
# Core Definition
A linear transformation T: V' -> V between representation spaces is G-invariant if T(gv') = gT(v'), or equivalently T o rho'_g = rho_g o T, for all g in G (Artin, (10.7.1), p. 320). In matrix form: MR'_g = R_g M (10.7.3). The averaging process can produce G-invariant maps from arbitrary ones: T-tilde = (1/|G|) sum_g g^{-1} T(g -) (10.7.7).
# Prerequisites
- **Group representation** — G-invariance relates two representations
# Key Properties
1. T(gv') = gT(v') for all g
2. Kernel and image are G-invariant subspaces (Lemma 10.7.4)
3. Any linear transformation can be averaged to produce a G-invariant one
4. Trace is preserved by averaging (Proposition 10.7.10)
5. Schur's Lemma classifies these maps between irreducibles
# Examples
**Example 1** (p. 320): An isomorphism of representations (10.1.16) is a bijective G-invariant linear transformation.
# Relationships
## Enables
- **Schur's lemma** — Characterizes G-invariant maps between irreducibles
# Source Reference
Chapter 10: Group Representations, Section 10.7, pages 320-322.
# Verification Notes
- Definition source: Direct from (10.7.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
