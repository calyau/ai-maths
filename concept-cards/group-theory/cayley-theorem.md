---
# === CORE IDENTIFICATION ===
concept: Cayley's Theorem
slug: cayley-theorem

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 16
section: "Homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cayley representation theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - monomorphism
extends: []
related:
  - left-coset
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can every group be realized as a permutation group?"
  - "How does Cayley's theorem embed a group into a symmetric group?"
---

# Quick Definition

Every group $G$ can be embedded into its own symmetric group $\mathrm{Sym}(G)$ via left multiplication. A finite group of order $n$ is isomorphic to a subgroup of $S_n$.

# Core Definition

"There is a canonical injective homomorphism $\alpha: G \to \mathrm{Sym}(G)$." (Milne, Theorem 1.22, p. 16)

The map sends $a \in G$ to the left multiplication $a_L: x \mapsto ax$, and $(ab)_L = a_L \circ b_L$.

# Prerequisites

- **Homomorphism** — The Cayley map is a homomorphism
- **Monomorphism** — The map is injective (by the cancellation law)

# Key Properties

1. The map $a \mapsto a_L$ is a homomorphism: $(ab)_L = a_L \circ b_L$
2. It is injective because of the cancellation law
3. For finite $G$ of order $n$, this gives $G \hookrightarrow S_n$ (Corollary 1.23)

# Construction / Recognition

## The Cayley Embedding:
1. For each $a \in G$, define $a_L: G \to G$ by $a_L(x) = ax$
2. Verify $a_L$ is a bijection (it has inverse $(a^{-1})_L$)
3. The map $a \mapsto a_L$ is the desired injection $G \hookrightarrow \mathrm{Sym}(G)$

# Context & Application

Cayley's theorem is conceptually important: it shows every abstract group is a concrete permutation group. However, as Milne notes, "$S_n$ is too large to be manageable" for most purposes (p. 17).

# Examples

**Example 1** (p. 16): For $a \in G$, the left multiplication $a_L(x) = ax$ satisfies $(a_L \circ b_L)(x) = a(bx) = (ab)x = (ab)_L(x)$.

**Example 2** (p. 17): Corollary 1.23 — list the elements of a finite group as $a_1, \ldots, a_n$ to embed $G$ into $S_n$.

# Relationships

## Builds Upon
- **homomorphism** — the Cayley map is a homomorphism
- **monomorphism** — the Cayley map is injective

## Enables
- Realization of abstract groups as permutation groups

# Common Errors

- **Error**: Thinking Cayley's theorem gives a practical way to study groups
  **Correction**: The embedding into $S_n$ is usually too large; better embeddings exist (see 4.22)

# Common Confusions

- **Confusion**: Confusing left and right regular representations
  **Clarification**: Milne uses left multiplication; right multiplication $a_R(x) = xa$ gives an anti-homomorphism

# Source Reference

Chapter 1, Theorem 1.22, Corollary 1.23, pages 16-17.

# Verification Notes

- Definition source: Direct from Theorem 1.22
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
