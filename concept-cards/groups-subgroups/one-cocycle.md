---
# === CORE IDENTIFICATION ===
concept: 1-Cocycle
slug: one-cocycle

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 384
section: "The cohomology of algebraic groups; applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - 1-cocycle
  - crossed homomorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
extends: []
related:
  - noncommutative-galois-cohomology
  - cohomology-set
  - form-of-algebraic-group
contrasts_with:
  - principal-one-cocycle

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

A 1-cocycle of a group $\Gamma$ in a $\Gamma$-group $A$ is a map $\sigma \mapsto a_\sigma$ from $\Gamma$ to $A$ satisfying the cocycle condition $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$ for all $\sigma, \tau \in \Gamma$.

# Core Definition

"A mapping $\sigma \mapsto a_\sigma$ of $\Gamma$ into $A$ is said to be a 1-cocycle of $\Gamma$ in $A$ if the relation $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$ holds for all $\sigma, \tau \in \Gamma$." (Milne, p. 384)

Two 1-cocycles $(a_\sigma)$ and $(b_\sigma)$ are equivalent if there exists $c \in A$ such that $b_\sigma = c^{-1} \cdot a_\sigma \cdot \sigma c$ for all $\sigma \in \Gamma$. A 1-cocycle of the form $\sigma \mapsto b^{-1} \cdot \sigma b$ for some $b \in A$ is called a *principal* 1-cocycle (or coboundary).

# Prerequisites

- **Group action** — The cocycle condition involves the action of $\Gamma$ on $A$

# Key Properties

1. The cocycle condition $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$ ensures compatibility with the group operation on $\Gamma$
2. Setting $\sigma = \tau = 1$ gives $a_1 = 1$
3. The equivalence relation $b_\sigma = c^{-1} \cdot a_\sigma \cdot \sigma c$ generalizes conjugation
4. Principal cocycles form the distinguished class in $H^1(\Gamma, A)$
5. For profinite $\Gamma$, one requires cocycles to be continuous

# Construction / Recognition

## To Construct a 1-Cocycle from a Form:
1. Given objects $X_0$ and $X$ over $k$ with an isomorphism $f: X_{0K} \to X_K$ over $K$
2. Define $a_\sigma = f^{-1} \circ \sigma f$ for each $\sigma \in \Gamma = \mathrm{Gal}(K/k)$
3. Verify: $a_\sigma \cdot \sigma a_\tau = (f^{-1} \circ \sigma f)(\sigma f^{-1} \circ \sigma\tau f) = f^{-1} \circ \sigma\tau f = a_{\sigma\tau}$

## To Recognize:
1. Check that the map $\sigma \mapsto a_\sigma$ satisfies $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$ for all $\sigma, \tau$

# Context & Application

1-cocycles are the basic objects whose equivalence classes form the cohomology set $H^1(\Gamma, A)$. They arise naturally when comparing two objects over $k$ that become isomorphic over a Galois extension: the "transition data" $a_\sigma = f^{-1} \circ \sigma f$ automatically satisfies the cocycle condition.

# Examples

**Example 1** (p. 386): Given a bilinear form $(V, \phi)$ over $k$ isomorphic to $(V_0, \phi_0)$ over $K$, choosing an isomorphism $f: (V_0, \phi_0)_K \to (V, \phi)_K$ produces a 1-cocycle $a_\sigma = f^{-1} \circ \sigma f$ in the automorphism group $\mathcal{A}(K)$.

**Example 2** (p. 389): For forms of an algebraic group $G_0$, choosing an isomorphism $f: G_{0K} \to G_K$ yields a 1-cocycle $a_\sigma = f^{-1} \circ \sigma f$ in $\mathrm{Aut}(G_{0K})$.

# Relationships

## Builds Upon
- **Group action** — the twisted action $\sigma a_\tau$ is essential to the cocycle condition

## Enables
- **Cohomology set** — $H^1(\Gamma, A)$ is the set of equivalence classes of 1-cocycles
- **Form of algebraic group** — cocycles encode the descent data for forms

## Contrasts With
- **Principal 1-cocycle** — coboundaries $\sigma \mapsto b^{-1} \cdot \sigma b$ are the trivial cocycles

# Common Errors

- **Error**: Forgetting the $\Gamma$-action in the cocycle condition, writing $a_{\sigma\tau} = a_\sigma \cdot a_\tau$
  **Correction**: The correct condition is $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$, involving the twisted action

# Common Confusions

- **Confusion**: Thinking 1-cocycles must be group homomorphisms
  **Clarification**: 1-cocycles are "crossed homomorphisms" — they reduce to homomorphisms only when $\Gamma$ acts trivially on $A$

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1a, page 384.

# Verification Notes

- Definition source: Direct quote from p. 384
- Confidence: HIGH — explicit definition with clear notation
- Uncertainties: None
- Cross-reference status: Verified
