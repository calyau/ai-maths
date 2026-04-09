---
concept: Isomorphism as Equivalence Relation
slug: isomorphism-equivalence-relation
category: morphisms
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Isomorphisms"
chapter_number: 9
pdf_page: 130
section: "9.1 Definition and Examples"
extraction_confidence: high
aliases: []
prerequisites:
  - group-isomorphism
extends: []
related:
  - isomorphism-properties
contrasts_with: []
answers_questions:
  - "Is isomorphism an equivalence relation?"
---

# Quick Definition

Group isomorphism defines an equivalence relation on the class of all groups: it is reflexive ($G \cong G$ via identity), symmetric ($G \cong H$ implies $H \cong G$ via $\phi^{-1}$), and transitive ($G \cong H$ and $H \cong K$ imply $G \cong K$ via composition).

# Core Definition

**Theorem 9.10:** "The isomorphism of groups determines an equivalence relation on the class of all groups" (Judson, p. 130). This justifies classifying groups "up to isomorphism."

# Prerequisites

- **Group Isomorphism** — The relation being analyzed

# Key Properties

1. Reflexive: the identity map $\text{id} : G \to G$ is an isomorphism
2. Symmetric: $\phi^{-1}$ is an isomorphism when $\phi$ is
3. Transitive: $\psi \circ \phi$ is an isomorphism when both $\psi$ and $\phi$ are
4. Equivalence classes are "isomorphism classes" of groups

# Construction / Recognition

## To Verify:
1. Reflexivity: $\text{id}_G$ is trivially an isomorphism
2. Symmetry: from Theorem 9.6(1), $\phi^{-1}$ is an isomorphism
3. Transitivity: composition of bijective homomorphisms is a bijective homomorphism

# Context & Application

This theorem justifies the fundamental approach in group theory: instead of studying individual groups, we classify isomorphism classes. Two groups in the same class are "the same" algebraically.

# Examples

**Example 1** (p. 130): We say "the infinite cyclic group" (rather than "an infinite cyclic group") because all infinite cyclic groups form a single isomorphism class.

# Relationships

## Builds Upon
- **Group Isomorphism** — The relation

## Related
- **Isomorphism Properties** — Properties that are constant within equivalence classes

# Common Errors

- **Error**: Thinking there is only one isomorphism between two isomorphic groups
  **Correction**: There may be many isomorphisms; $U(8) \cong U(12)$ has multiple isomorphisms (Example 9.4)

# Common Confusions

- **Confusion**: Confusing "equivalence relation on groups" with an equivalence relation on elements
  **Clarification**: This is an equivalence relation on the *class of all groups*, not on elements within a group

# Source Reference

Chapter 9: Isomorphisms, Section 9.1, Theorem 9.10, page 130.

# Verification Notes

- Definition source: Direct from Theorem 9.10
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
