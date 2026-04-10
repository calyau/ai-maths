---
# === CORE IDENTIFICATION ===
concept: Noncommutative Galois Cohomology
slug: noncommutative-galois-cohomology

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
  - nonabelian cohomology
  - "H^1 of a group"
  - non-commutative cohomology

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - algebraic-group
extends: []
related:
  - one-cocycle
  - cohomology-set
  - form-of-algebraic-group
  - galois-cohomology-of-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

Noncommutative Galois cohomology extends the classical cohomology of groups to the setting where the coefficient group $A$ is not necessarily abelian. The set $H^1(\Gamma, A)$ classifies equivalence classes of 1-cocycles and is a pointed set rather than a group.

# Core Definition

Let $\Gamma$ be a group and $A$ a $\Gamma$-group (a group with a $\Gamma$-action respecting the group structure). The zeroth cohomology is $H^0(\Gamma, A) = A^\Gamma$, the fixed-point set. The first cohomology $H^1(\Gamma, A)$ is defined as the set of equivalence classes of 1-cocycles of $\Gamma$ in $A$. "In general $H^1(\Gamma, A)$ is not a group unless $A$ is commutative, but it has a distinguished element, namely, the class of 1-cocycles of the form $\sigma \mapsto b^{-1} \cdot \sigma b$, $b \in A$ (the *principal* 1-cocycles)." (Milne, p. 384)

When $\Gamma = \mathrm{Gal}(k^{\mathrm{al}}/k)$, one requires the cocycles to be continuous (equivalently, to factor through finite Galois extensions), giving $H^1(\Gamma, A) = \varinjlim H^1(\mathrm{Gal}(K/k), A^{\Gamma_K})$.

# Prerequisites

- **Group action** — $H^0$ and $H^1$ are defined via the action of $\Gamma$ on $A$
- **Algebraic group** — The main application is to $A = G(k^{\mathrm{al}})$ for an algebraic group $G$

# Key Properties

1. $H^0(\Gamma, A) = A^\Gamma$ is the set (or group) of $\Gamma$-fixed elements
2. $H^1(\Gamma, A)$ is a pointed set with distinguished element (the class of principal cocycles)
3. $H^1(\Gamma, A)$ is a group if and only if $A$ is commutative
4. An exact sequence $1 \to A' \to A \to A'' \to 1$ of $\Gamma$-groups yields an exact sequence of cohomology sets (Proposition 1.1)
5. For profinite $\Gamma$, one uses continuous cocycles and takes a direct limit over finite Galois extensions

# Construction / Recognition

## To Compute $H^1(\Gamma, A)$:
1. Identify the $\Gamma$-group $A$ and the action of $\Gamma$
2. Determine the set of 1-cocycles $\sigma \mapsto a_\sigma$ satisfying $a_{\sigma\tau} = a_\sigma \cdot \sigma a_\tau$
3. Identify equivalence classes under the relation $b_\sigma = c^{-1} \cdot a_\sigma \cdot \sigma c$
4. The result is a pointed set with the class of principal cocycles as distinguished element

# Context & Application

Noncommutative Galois cohomology is the primary tool for classifying forms of algebraic objects over a field $k$. Given an object $X_0$ over $k$, the objects over $k$ that become isomorphic to $X_0$ over a Galois extension $K$ are classified by $H^1(\mathrm{Gal}(K/k), \mathrm{Aut}(X_{0K}))$. This applies to algebraic groups, bilinear forms, and algebras.

# Examples

**Example 1** (p. 388): $H^1(\Gamma, \mathrm{GL}_n(K)) = 1$ for any finite Galois extension $K/k$. This follows because the only $k$-vector space $V$ with $K \otimes_k V \approx K^n$ has dimension $n$ and is therefore isomorphic to $k^n$.

**Example 2** (p. 388): $H^1(\Gamma, \mathrm{SL}_n(K)) = 1$, proved via the exact sequence $1 \to \mathrm{SL}_n \to \mathrm{GL}_n \xrightarrow{\det} K^\times \to 1$.

**Example 3** (p. 388): $H^1(\Gamma, \mathrm{Sp}(K)) = 1$ because all nondegenerate alternating forms of the same dimension are isomorphic.

# Relationships

## Builds Upon
- **Group action** — cohomology measures the obstruction to descending $\Gamma$-equivariant data

## Enables
- **Form of algebraic group** — $H^1$ classifies forms
- **Galois cohomology of algebraic groups** — specialization to $\Gamma = \mathrm{Gal}(k^{\mathrm{al}}/k)$
- **Congruence subgroup problem** — cohomological methods appear in the analysis

## Related
- **One-cocycle** — the basic objects classified by $H^1$
- **Cohomology set** — $H^1$ as a pointed set

# Common Errors

- **Error**: Treating $H^1(\Gamma, A)$ as a group when $A$ is noncommutative
  **Correction**: $H^1$ is only a pointed set in the noncommutative case; it has a distinguished element but no group structure

# Common Confusions

- **Confusion**: Believing that $H^1 = 1$ always holds
  **Clarification**: $H^1 = 1$ for $\mathrm{GL}_n$, $\mathrm{SL}_n$, and $\mathrm{Sp}$ but can be very large for orthogonal groups (Remark 1.9)

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1a "Non-commutative cohomology," pages 384-385.

# Verification Notes

- Definition source: Direct from p. 384
- Confidence: HIGH — explicit definitions and notation throughout
- Uncertainties: None
- Cross-reference status: Verified against Propositions 1.1, 1.6, 1.7, 1.8
