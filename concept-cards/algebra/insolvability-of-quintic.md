---
concept: Insolvability of the Quintic
slug: insolvability-of-quintic
category: galois-theory
subcategory: applications
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.12 Quintic Equations"
extraction_confidence: high
aliases:
  - "Abel-Ruffini theorem"
  - "unsolvability of the quintic"
prerequisites:
  - solvability-by-radicals
  - galois-group
  - simple-group
extends: []
related:
  - symmetric-group
  - alternating-group
contrasts_with: []
answers_questions:
  - "Why can't the general quintic be solved by radicals?"
  - "How do I determine if an equation is solvable by radicals?"
---

# Quick Definition

There exist irreducible quintic polynomials over Q whose roots cannot be expressed using radicals (nth roots) starting from the coefficients. This happens because their Galois groups (A_5 or S_5) are not solvable groups.

# Core Definition

Let f be an irreducible polynomial of degree 5 over a subfield F of C whose Galois group G is either A_5 or S_5. Then the roots of f are not solvable over F (Artin, Theorem 16.12.4). The proof uses the fact that A_5 is a simple group: a Galois extension of prime degree p over any intermediate field cannot reduce G = A_5 to a smaller group, because A_5 has no normal subgroups other than {1} and itself.

# Prerequisites

- **Solvability by radicals** -- The concept being negated
- **Galois group** -- Must be A_5 or S_5
- **Simple group** -- A_5 is simple, which blocks the radical tower

# Key Properties

1. If an irreducible quintic over Q has exactly three real roots, its Galois group is S_5 (Corollary 16.12.6)
2. A subgroup of S_5 containing a 5-cycle and a transposition equals S_5 (Lemma 16.12.5)
3. The key obstruction: A_5 is simple, so no chain of Galois extensions of prime degree can resolve it
4. Polynomials of degree at most 4 are always solvable (16.12.3), making 5 the critical degree

# Context & Application

This is the most celebrated application of Galois theory, resolving a 200+ year old problem. It shows that there is no "quintic formula" analogous to the quadratic or cubic formulas. The proof beautifully connects algebra (group theory) to analysis (root counting).

# Examples

**Example 1** (p. 514): f(x) = x^5 - 16x + 2 is irreducible over Q and has exactly three real roots. By Corollary 16.12.6, G = S_5, so the roots are not solvable.

**Example 2** (p. 514): f(x) = x^5 - 16x = x(x^2-4)(x^2+4) has three real roots but is reducible. Adding a small constant (like 2) makes it irreducible while preserving the root count.

# Relationships

## Builds Upon
- **Solvability by radicals** -- This is a non-solvability result
- **Galois group** -- The Galois group determines solvability

## Related
- **Alternating group** -- A_5 is the obstruction (being simple)
- **Symmetric group** -- S_5 contains A_5 as a normal subgroup

# Common Confusions

- **Confusion**: Thinking no quintic can be solved by radicals
  **Clarification**: Many specific quintics ARE solvable (e.g., x^5 - 2). Only those with unsolvable Galois groups cannot be solved.

# Source Reference

Chapter 16: Galois Theory, Section 16.12, pages 510-515. Theorem 16.12.4, Corollary 16.12.6.

# Verification Notes

- Definition source: Direct from Artin, Theorem 16.12.4
- Confidence rationale: Complete proof with explicit example
- Uncertainties: None
- Cross-reference status: Verified
