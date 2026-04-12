---
# === CORE IDENTIFICATION ===
concept: Free Action on Tree Theorem
slug: free-action-on-tree-theorem

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Trees and the Nielsen-Schreier Theorem"
chapter_number: 28
pdf_page: 180
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 28.3"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tree
  - group-action-on-a-graph
  - reference-tree
  - free-group
extends: []
related:
  - nielsen-schreier-theorem
  - cayley-graph
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does a free action on a tree produce a free group?"
---

# Quick Definition

If a group G acts freely on a tree, then G is a free group. This is Theorem 28.3, and it is the key lemma for proving the Nielsen-Schreier theorem.

# Core Definition

"(28.3) Theorem. If G acts freely on a tree then G is a free group" (Armstrong, Ch. 28, p. 184). The proof constructs a free set of generators X for G using a reference tree Lambda. For each edge alpha in A_* (edges not in Lambda with initial vertex in Lambda), a unique group element g_alpha is defined, and from each pair {g_alpha, g_alpha^{-1}} one representative is chosen for X.

# Prerequisites

- **Tree** -- The group acts on a tree
- **Group action on a graph** -- The action must be free (trivial vertex stabilizers)
- **Reference tree** -- Used to construct the free generators
- **Free group** -- The conclusion

# Key Properties

1. The set X constructed from the reference tree freely generates G
2. Each non-identity g in G can be uniquely decomposed along geodesics from v to g(v)
3. The proof shows both that X generates G and that the representation as a reduced word is unique
4. The proof uses the fact that geodesics in trees are unique
5. The construction is canonical given the choice of reference tree and basepoint

# Construction / Recognition

## Proof Outline (Armstrong, pp. 184-186)
1. Choose reference tree Lambda and basepoint v in Lambda
2. Let A_* = edges not in Lambda with initial vertex in Lambda
3. For each alpha in A_*, define g_alpha: the unique group element sending the Lambda-representative to t(alpha)
4. Edges and group elements come in pairs: alpha' = g_alpha^{-1}(alpha-bar), g_{alpha'} = g_alpha^{-1}
5. Choose one from each pair to form X
6. For any g in G - {e}, trace the geodesic from v to g(v), applying g_alpha^{-1} each time the path leaves Lambda
7. This process terminates (path shortens at each step) and produces g = g_alpha g_beta ... g_nu
8. Show this decomposition gives a unique reduced word in X

# Context & Application

This theorem is the geometric heart of Armstrong's chapter. It translates the problem of showing a group is free into the geometric problem of finding a tree on which it acts freely. Combined with Theorem 28.1 (Cayley graphs of free groups are trees), it immediately yields the Nielsen-Schreier theorem.

# Examples

**Example 1** (p. 181, Example (ii)): Z acts freely on the integer line (a tree). The theorem confirms Z is free (on one generator).

**Example 2** (Exercise 28.6, p. 186): Armstrong asks the reader to trace the proof for Z acting on the integer line and for F_2 acting on its Cayley tree.

# Relationships

## Builds Upon
- **Reference tree** -- The proof uses reference trees
- **Group action on a graph** -- The action must be free

## Enables
- **Nielsen-Schreier theorem** -- Immediate corollary

## Related
- **Cayley graph** -- Cayley graphs of free groups provide the trees

# Common Errors

- **Error**: Forgetting the "freely" condition and applying the theorem to non-free actions
  **Correction**: The theorem fails for non-free actions; Example (i) shows Z_3 acting non-freely on a tree (Z_3 is not free)

# Common Confusions

- **Confusion**: Thinking any action on a tree makes a group free
  **Clarification**: The action must be free (trivial vertex stabilizers); non-free actions on trees arise for non-free groups

# Source Reference

Chapter 28: Trees and the Nielsen-Schreier Theorem, Theorem 28.3 and proof, pages 184-186 (pdf pp. 184-186).

# Verification Notes

- Theorem: Directly quoted from Armstrong p. 184
- Proof: Complete in source pp. 184-186
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
