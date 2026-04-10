---
# === CORE IDENTIFICATION ===
concept: Cohomology Set
slug: cohomology-set

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
  - "H^1(Gamma, A)"
  - first cohomology set
  - pointed cohomology set

# === TYPED RELATIONSHIPS ===
prerequisites:
  - one-cocycle
  - group-action
extends: []
related:
  - noncommutative-galois-cohomology
  - form-of-algebraic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Galois cohomology of algebraic groups?"
  - "How does Galois cohomology classify forms of algebraic groups?"
---

# Quick Definition

The cohomology set $H^1(\Gamma, A)$ is the set of equivalence classes of 1-cocycles of a group $\Gamma$ in a $\Gamma$-group $A$. It is a pointed set (with the class of principal cocycles as distinguished element) and is a group only when $A$ is abelian.

# Core Definition

$H^1(\Gamma, A)$ is defined as the set of equivalence classes of 1-cocycles, where two 1-cocycles $(a_\sigma)$ and $(b_\sigma)$ are equivalent if there exists $c \in A$ with $b_\sigma = c^{-1} \cdot a_\sigma \cdot \sigma c$ for all $\sigma \in \Gamma$ (Milne, p. 384).

An exact sequence $1 \to A' \to A \to A'' \to 1$ of $\Gamma$-groups gives rise to an exact sequence of cohomology sets:
$$1 \to H^0(\Gamma, A') \to H^0(\Gamma, A) \to H^0(\Gamma, A'') \to H^1(\Gamma, A') \to H^1(\Gamma, A) \to H^1(\Gamma, A'')$$
(Proposition 1.1, p. 384).

# Prerequisites

- **1-cocycle** — $H^1$ is defined as equivalence classes of 1-cocycles
- **Group action** — The equivalence relation and cocycle condition use the $\Gamma$-action

# Key Properties

1. $H^1(\Gamma, A)$ is a pointed set with distinguished element (class of coboundaries)
2. $H^1(\Gamma, A)$ is a group if $A$ is commutative
3. Compatible homomorphisms $f: A \to B$, $g: \Delta \to \Gamma$ induce maps $H^1(\Gamma, A) \to H^1(\Delta, B)$
4. Short exact sequences of $\Gamma$-groups yield long exact sequences of cohomology sets
5. Exactness at $H^1(\Gamma, A')$ means the fiber over the distinguished element equals the image of $H^0(\Gamma, A'')$

# Construction / Recognition

## To Compute:
1. Determine all 1-cocycles $\sigma \mapsto a_\sigma$ satisfying $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$
2. Partition into equivalence classes under the relation $b_\sigma \sim a_\sigma$ iff $b_\sigma = c^{-1} a_\sigma \cdot \sigma c$
3. The resulting set of classes is $H^1(\Gamma, A)$

# Context & Application

Cohomology sets are the fundamental classifying objects in the theory of forms. The key theorems (1.5, 1.10) show that $H^1(\Gamma, \mathcal{A}(K))$ classifies isomorphism classes of objects over $k$ that become isomorphic to a given object over a Galois extension $K/k$.

# Examples

**Example 1** (p. 388): $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ (trivial, one element).

**Example 2** (p. 388): $H^1(\Gamma, \mathrm{O}(K))$ classifies nondegenerate quadratic spaces over $k$ becoming isomorphic to a given one over $K$. This can be a very large set (Remark 1.9).

# Relationships

## Builds Upon
- **One-cocycle** — $H^1$ consists of equivalence classes of 1-cocycles

## Enables
- **Form of algebraic group** — forms are classified by $H^1$
- **Inner form** — inner forms correspond to a specific subset of $H^1$

## Related
- **Noncommutative Galois cohomology** — $H^1$ is the central object of this theory

# Common Errors

- **Error**: Assuming $H^1$ always has a group structure
  **Correction**: $H^1(\Gamma, A)$ is only a pointed set when $A$ is nonabelian

# Common Confusions

- **Confusion**: Confusing "exactness" for pointed sets with exactness for groups
  **Clarification**: Exactness at $H^1$ terms means the fiber over the distinguished element equals the image, not kernel equals image in the usual group-theoretic sense

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1a, pages 384-385. Proposition 1.1.

# Verification Notes

- Definition source: Direct from pp. 384-385
- Confidence: HIGH — explicit definition
- Uncertainties: None
- Cross-reference status: Verified
