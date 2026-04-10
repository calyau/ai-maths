---
# === CORE IDENTIFICATION ===
concept: Form of an Algebraic Group
slug: form-of-algebraic-group

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
pdf_page: 389
section: "Classifying the forms of an algebraic group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - twisted form
  - K/k-form

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-group
  - noncommutative-galois-cohomology
  - one-cocycle
extends: []
related:
  - inner-form
  - galois-cohomology-of-algebraic-groups
  - cohomology-set
contrasts_with:
  - split-reductive-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Galois cohomology classify forms of algebraic groups?"
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

A form of an algebraic group $G_0$ over $k$ is an algebraic group $G$ over $k$ that becomes isomorphic to $G_0$ over a field extension. The isomorphism classes of such forms are classified by the Galois cohomology set $H^1(\Gamma, \mathrm{Aut}(G_{0K}))$.

# Core Definition

Let $G_0$ be an algebraic group over $k$, $K/k$ a finite Galois extension with group $\Gamma$, and $\mathcal{A}(K)$ the group of automorphisms of $G_{0K}$ with $\Gamma$-action $\sigma\alpha = \sigma \circ \alpha \circ \sigma^{-1}$.

"The cohomology set $H^1(\Gamma, \mathcal{A}(K))$ classifies the isomorphism classes of algebraic groups $G$ over $k$ that become isomorphic to $G_0$ over $K$." (Theorem 1.10, Milne, p. 389)

Given such a $G$ and an isomorphism $f: G_{0K} \to G_K$, the 1-cocycle $a_\sigma = f^{-1} \circ \sigma f$ determines the class of $G$ in $H^1(\Gamma, \mathcal{A}(K))$.

# Prerequisites

- **Algebraic group** — Forms are algebraic groups related by base change
- **Noncommutative Galois cohomology** — The classification uses $H^1$
- **1-cocycle** — The transition data defining a form is a 1-cocycle

# Key Properties

1. The trivial class in $H^1$ corresponds to the isomorphism class of $G_0$ itself
2. Surjectivity of the classifying map is proved by twisting: a cocycle $(a_\sigma)$ defines a new semilinear action ${}^\sigma a = a_\sigma \circ \sigma a$ on the Hopf algebra $K \otimes_k \mathcal{O}(G_0)$
3. The fixed subalgebra under the twisted action is the coordinate ring of the new form
4. All forms over $k^{\mathrm{al}}$ are captured by $H^1(k, \mathrm{Aut}(G_{0,k^{\mathrm{al}}}))$ (1.15)
5. $H^1(k, \mathrm{GL}_n) = 1$ means $\mathrm{GL}_n$ has no nontrivial forms

# Construction / Recognition

## To Construct a Form from a Cocycle:
1. Start with $G_0$ over $k$ and a 1-cocycle $(a_\sigma)$ in $\mathrm{Aut}(G_{0K})$
2. Define a twisted semilinear action on $A = K \otimes_k \mathcal{O}(G_0)$ by ${}^\sigma a = a_\sigma(\sigma a)$
3. Take the fixed subalgebra $B = \{a \in A \mid {}^\sigma a = a\}$
4. The Hopf algebra structure on $A$ restricts to $B$, giving a new algebraic group $G$ over $k$

## To Recognize:
1. Two algebraic groups $G$, $G'$ over $k$ are forms of each other if $G_K \cong G'_K$ for some Galois extension $K/k$

# Context & Application

The classification of forms is central to understanding algebraic groups over non-algebraically closed fields. Over an algebraically closed field, split groups are classified by root data; over an arbitrary field, one must additionally classify all forms of each split group.

# Examples

**Example 1** (pp. 382-383): The forms of $\mathrm{GL}_2$ over $k$ are the groups $G(a,b)$ with $G(R) = (R \otimes \mathbb{H}(a,b))^\times$, where $\mathbb{H}(a,b)$ is a quaternion algebra. Over $\mathbb{R}$ there are exactly two forms. Over $\mathbb{Q}$ there are infinitely many, classified by even-cardinality subsets of primes $\cup \{\infty\}$.

**Example 2** (p. 390): $H^1(k, \mathrm{GL}_n) = 1$, $H^1(k, \mathrm{SL}_n) = 1$, $H^1(k, \mathrm{Sp}_n) = 1$ (1.11-1.13), meaning these groups have no nontrivial forms.

**Example 3** (p. 390): $H^1(k, \mathrm{O}(\phi))$ classifies nondegenerate quadratic spaces of a given dimension (1.14).

# Relationships

## Builds Upon
- **Noncommutative Galois cohomology** — forms are classified by $H^1$
- **One-cocycle** — transition data for a form is a cocycle

## Enables
- **Inner form** — a special type of form classified by $H^1(k, G^{\mathrm{ad}})$
- **Anisotropic kernel** — understanding non-split groups requires forms

## Related
- **Galois cohomology of algebraic groups** — the framework for classifying forms

## Contrasts With
- **Split reductive group** — the split form is the distinguished element in $H^1$

# Common Errors

- **Error**: Assuming every algebraic group has only finitely many forms
  **Correction**: $\mathrm{GL}_2$ over $\mathbb{Q}$ has infinitely many forms (from quaternion algebras)

# Common Confusions

- **Confusion**: Confusing forms with subgroups
  **Clarification**: A form of $G_0$ is a separate algebraic group that becomes isomorphic to $G_0$ only after base change, not a subgroup of $G_0$

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Sections 1b-1c, pages 385-390. Theorems 1.5, 1.10.

# Verification Notes

- Definition source: Theorem 1.10, directly stated on p. 389
- Confidence: HIGH — explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
