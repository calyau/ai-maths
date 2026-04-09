---
# === CORE IDENTIFICATION ===
concept: Inner Automorphism Group
slug: inner-automorphism-group

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
aliases:
  - "Inn(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - inner-automorphism
  - automorphism-group
extends:
  - inner-automorphism
related:
  - centre-of-group
  - outer-automorphism-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an inner and outer automorphism?"
---

# Quick Definition

$\operatorname{Inn}(G)$ is the group of all inner automorphisms of $G$, isomorphic to $G/Z(G)$.

# Core Definition

The image of the homomorphism $g \mapsto i_g : G \to \operatorname{Aut}(G)$ is denoted $\operatorname{Inn}(G)$ (Milne, p. 42). Its kernel is the centre $Z(G)$, yielding the isomorphism $G/Z(G) \to \operatorname{Inn}(G)$.

# Prerequisites

- **Inner automorphism** — $\operatorname{Inn}(G)$ consists of all inner automorphisms
- **Automorphism group** — $\operatorname{Inn}(G)$ is a subgroup of $\operatorname{Aut}(G)$

# Key Properties

1. $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$
2. $\operatorname{Inn}(G) \simeq G/Z(G)$
3. $\operatorname{Inn}(G) = \{1\}$ if and only if $G$ is abelian
4. $\alpha \circ i_g \circ \alpha^{-1} = i_{\alpha(g)}$ for all $\alpha \in \operatorname{Aut}(G)$

# Context & Application

$\operatorname{Inn}(G)$ measures the non-commutativity of $G$. It is always a normal subgroup of $\operatorname{Aut}(G)$, and the quotient $\operatorname{Aut}(G)/\operatorname{Inn}(G)$ is the outer automorphism group.

# Examples

**Example 1** (p. 42): For $G = \mathbb{F}_p^n$, $\operatorname{Inn}(G) = \{1\}$ since $G$ is commutative.

**Example 2** (p. 42): For the quaternion group, $\operatorname{Inn}(Q) \simeq Q/\langle a^2 \rangle \approx C_2 \times C_2$.

# Relationships

## Builds Upon
- **inner-automorphism** — Elements of $\operatorname{Inn}(G)$
- **centre-of-group** — Kernel of $G \to \operatorname{Inn}(G)$

## Enables
- **outer-automorphism-group** — $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$
- **complete-group** — Requires $\operatorname{Inn}(G) = \operatorname{Aut}(G)$

# Common Errors

- **Error**: Thinking $\operatorname{Inn}(G)$ can be non-normal in $\operatorname{Aut}(G)$
  **Correction**: $\operatorname{Inn}(G)$ is always normal in $\operatorname{Aut}(G)$

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of groups", page 42.

# Verification Notes

- Definition source: Direct from p. 42
- Confidence: HIGH — explicit definition
- Uncertainties: None
