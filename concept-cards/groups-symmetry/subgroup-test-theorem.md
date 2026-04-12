---
# === CORE IDENTIFICATION ===
concept: Subgroup Test Theorem
slug: subgroup-test-theorem

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Subgroups and Generators"
chapter_number: 5
pdf_page: 27
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - one-step subgroup test
  - "Theorem 5.1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - inverse-element
extends: []
related:
  - intersection-of-subgroups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a subgroup?"
  - "How do I find all subgroups of a finite group?"
---

# Quick Definition

The subgroup test theorem (Theorem 5.1) states that a non-empty subset H of a group G is a subgroup if and only if xy^{-1} belongs to H whenever x and y belong to H. This provides a single condition to check instead of three.

# Core Definition

"**Theorem.** A non-empty subset H of a group G is a subgroup of G if and only if xy^{-1} belongs to H whenever x and y belong to H" (Armstrong, Theorem 5.1, Ch. 5, p. 31).

# Prerequisites

- **Subgroup** — The theorem characterizes subgroups
- **Inverse Element** — The test involves inverses

# Key Properties

1. The condition xy^{-1} in H implies closure, identity, and inverses all at once
2. H must be non-empty (this is a hypothesis)
3. From x in H: e = xx^{-1} in H (identity)
4. From e, x in H: x^{-1} = ex^{-1} in H (inverses)
5. From x, y^{-1} in H: xy = x(y^{-1})^{-1} in H (closure)

# Construction / Recognition

## To Apply the Test:
1. Verify H is non-empty
2. Take any x, y in H
3. Check that xy^{-1} is also in H
4. If this holds for all x, y, then H < G

## Proof Outline:
- (=>) If H is a subgroup: y^{-1} is in H (inverse), so xy^{-1} is in H (closure)
- (<=) If xy^{-1} in H for all x, y in H:
  - e = xx^{-1} in H (take y = x)
  - x^{-1} = ex^{-1} in H (take x = e)
  - xy = x(y^{-1})^{-1} in H (apply to x and y^{-1})

# Context & Application

The subgroup test simplifies subgroup verification from three checks to one. It is particularly useful in proofs where the subgroup property must be verified abstractly. For finite subsets, an even simpler test exists: H is a subgroup if and only if xy in H whenever x, y in H (Exercise 5.5).

# Examples

**Example 1** (p. 31-32): The proof derives all three subgroup conditions from the single condition xy^{-1} in H.

**Example 2** (Exercise 5.5): For finite non-empty subsets, checking only that xy in H for all x, y in H suffices (inverses and identity follow automatically).

# Relationships

## Builds Upon
- **Subgroup** — Characterizes subgroups

## Related
- **Intersection of Subgroups** — Theorem 5.2 uses similar techniques

# Common Errors

- **Error**: Forgetting to verify H is non-empty
  **Correction**: The empty set satisfies the condition vacuously but is not a subgroup

# Common Confusions

- **Confusion**: Thinking the test checks xy instead of xy^{-1}
  **Clarification**: The condition is xy^{-1} in H, not xy in H (though for finite subsets, xy in H suffices by Exercise 5.5)

# Source Reference

Chapter 5: Subgroups and Generators, Theorem 5.1, pages 24-25 (pdf pp. 31-32).

# Verification Notes

- Definition source: Direct quote of theorem statement from p. 31
- Confidence rationale: High — formally stated and proved
- Uncertainties: None
- Cross-reference status: Verified
