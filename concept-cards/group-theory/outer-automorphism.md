---
# === CORE IDENTIFICATION ===
concept: Outer Automorphism
slug: outer-automorphism

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: automorphisms
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 42
section: "Automorphisms of groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - inner-automorphism
  - automorphism
extends:
  - automorphism
related:
  - outer-automorphism-group
contrasts_with:
  - inner-automorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an inner and outer automorphism?"
---

# Quick Definition

An outer automorphism of $G$ is an automorphism that is not inner, i.e., not of the form $x \mapsto gxg^{-1}$ for any $g \in G$.

# Core Definition

An automorphism $\alpha$ of $G$ is outer if $\alpha \neq i_g$ for any $g \in G$, where $i_g$ denotes conjugation by $g$ (Milne, p. 42).

# Prerequisites

- **Inner automorphism** — Outer automorphisms are defined as "the remaining automorphisms"
- **Automorphism** — An outer automorphism is a specific kind of automorphism

# Key Properties

1. Outer automorphisms exist when $\operatorname{Inn}(G) \neq \operatorname{Aut}(G)$
2. All nontrivial automorphisms of an abelian group are outer
3. $S_6$ is the only symmetric group (besides $S_2$) having outer automorphisms (Example 3.4a)
4. An outer automorphism of $N$ can become the restriction of an inner automorphism of a larger group $G \supset N$ (Example 3.16)

# Context & Application

Outer automorphisms reflect symmetries of a group that cannot be realized by internal conjugation. Their existence or absence is a structural property. Notably, $S_n$ is complete (no outer automorphisms, trivial centre) for $n \neq 2, 6$.

# Examples

**Example 1** (p. 42): For $G = \mathbb{F}_p^n$, all nontrivial automorphisms are outer since $G$ is commutative.

**Example 2** (p. 43): $S_6$ has outer automorphisms: $\operatorname{Aut}(S_6)/\operatorname{Inn}(S_6) \simeq C_2$.

**Example 3** (p. 48): Any outer automorphism $\alpha$ of $N$ can be made inner in $G = N \rtimes_\theta C_\infty$ where $\theta$ sends a generator to $\alpha$.

# Relationships

## Contrasts With
- **inner-automorphism** — Given by conjugation; outer automorphisms are not

## Related
- **outer-automorphism-group** — $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$ measures outer automorphisms
- **complete-group** — Has no outer automorphisms

# Common Errors

- **Error**: Thinking the outer automorphism group $\operatorname{Out}(G)$ consists of outer automorphisms
  **Correction**: $\operatorname{Out}(G)$ is a quotient group; its non-identity elements are cosets, not individual automorphisms

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of groups", page 42.

# Verification Notes

- Definition source: Implicit from p. 42 definition of inner automorphisms
- Confidence: HIGH — explicit description
- Uncertainties: None
