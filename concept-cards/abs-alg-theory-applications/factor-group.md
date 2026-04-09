---
# === CORE IDENTIFICATION ===
concept: Factor Group
slug: factor-group

# === CLASSIFICATION ===
category: group-structure
subcategory: group-constructions
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 138
section: "Factor Groups and Normal Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "quotient group"
  - "G/N"
  - "G mod N"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - coset
extends:
  - group
related:
  - canonical-homomorphism
  - first-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a factor (quotient) group?"
  - "How do I construct a factor group?"
  - "How do normal subgroups relate to factor groups?"
---

# Quick Definition

If $N$ is a normal subgroup of $G$, the factor (or quotient) group $G/N$ is the group whose elements are the cosets of $N$ in $G$, with multiplication defined by $(aN)(bN) = abN$. Its order is $[G:N]$.

# Core Definition

"If $N$ is a normal subgroup of a group $G$, then the cosets of $N$ in $G$ form a group $G/N$ under the operation $(aN)(bN) = abN$. This group is called the **factor** or **quotient group** of $G$ and $N$" (Judson, p. 139). The order of $G/N$ is $[G:N]$, the index of $N$ in $G$ (Theorem 10.4).

# Prerequisites

- **Normal subgroup** — The subgroup $N$ must be normal for the coset multiplication to be well-defined
- **Coset** — The elements of the factor group are cosets of $N$

# Key Properties

1. The elements of $G/N$ are cosets $gN$ for $g \in G$
2. The group operation is $(aN)(bN) = abN$
3. The identity element is $N = eN$
4. The inverse of $gN$ is $g^{-1}N$
5. The order of $G/N$ equals $[G:N] = |G|/|N|$ when $G$ is finite
6. Normality of $N$ is required for the operation to be well-defined
7. If $G$ is abelian, then $G/N$ is abelian
8. If $G$ is cyclic, then $G/N$ is cyclic

# Construction / Recognition

## To Construct a Factor Group:
1. Verify that $N$ is a normal subgroup of $G$
2. List the distinct cosets of $N$ in $G$
3. Define multiplication by $(aN)(bN) = abN$
4. The identity is $N$ and inverse of $gN$ is $g^{-1}N$

## To Identify a Factor Group:
1. Elements are sets (cosets), not individual group elements
2. The number of elements equals the index $[G:N]$
3. Check if the result is isomorphic to a known group

# Context & Application

Factor groups are fundamental to group theory because they capture the "quotient structure" obtained by collapsing a normal subgroup to the identity. Every group homomorphism gives rise to a factor group via the First Isomorphism Theorem. Factor groups are essential for analyzing group structure, proving simplicity results, and understanding solvable groups.

# Examples

**Example 1** (p. 139): $S_3/N$ where $N = \{(1), (123), (132)\}$. The factor group has two elements: $N$ and $(12)N$. This group is isomorphic to $\mathbb{Z}_2$. The factor group captures parity information: multiplying two even or two odd permutations gives an even permutation.

**Example 2** (p. 140): $\mathbb{Z}/3\mathbb{Z}$ has three cosets: $0+3\mathbb{Z}$, $1+3\mathbb{Z}$, $2+3\mathbb{Z}$. Addition of cosets is given by $(k+3\mathbb{Z}) + (l+3\mathbb{Z}) = (k+l)+3\mathbb{Z}$.

**Example 3** (p. 140): $D_n/R_n \cong \mathbb{Z}_2$, where $R_n$ is the rotation subgroup. This has exactly two elements since $[D_n:R_n] = 2$.

# Relationships

## Builds Upon
- **Normal subgroup** — $N$ must be normal for $G/N$ to form a group
- **Coset** — Elements of $G/N$ are cosets

## Enables
- **Isomorphism theorems** — Factor groups are central to all isomorphism theorems
- **Solvable group** — Defined via a chain of factor groups being abelian
- **Simple group** — A group with no nontrivial factor groups

## Related
- **Canonical homomorphism** — The natural map $G \to G/N$ given by $g \mapsto gN$
- **First isomorphism theorem** — $G/\ker\phi \cong \phi(G)$

# Common Errors

- **Error**: Attempting to form $G/H$ when $H$ is not normal
  **Correction**: The coset operation $(aH)(bH) = abH$ is only well-defined when $H$ is normal in $G$

- **Error**: Treating elements of $G/N$ as elements of $G$ rather than as cosets
  **Correction**: "It is very important to remember that the elements in a factor group are sets of elements in the original group" (p. 139)

# Common Confusions

- **Confusion**: Thinking $G/N$ is a subset of $G$
  **Clarification**: $G/N$ is a group of cosets. Each element of $G/N$ is a set of elements from $G$

- **Confusion**: Believing $G/N \cong G$ minus $N$
  **Clarification**: $G/N$ captures the structure of $G$ modulo the equivalence induced by $N$

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Section 10.1, pages 139-140. Theorem 10.4 proves the factor group is well-defined.

# Verification Notes

- Definition source: Direct quote from p. 139
- Well-definedness proof: Theorem 10.4, p. 139
- Examples: All from source (Examples 10.5-10.7)
- Confidence: HIGH — explicit definition with full proof and examples
- Cross-reference status: Verified
