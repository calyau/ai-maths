---
# === CORE IDENTIFICATION ===
concept: Inner Automorphism
slug: inner-automorphism

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
  - conjugation automorphism

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism
  - conjugation
extends:
  - automorphism
related:
  - inner-automorphism-group
  - centre-of-group
contrasts_with:
  - outer-automorphism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an inner and outer automorphism?"
  - "What is an automorphism of a group?"
---

# Quick Definition

An inner automorphism of $G$ is conjugation by some element $g \in G$: the map $x \mapsto gxg^{-1}$.

# Core Definition

"For $g \in G$, the map $i_g$ 'conjugation by $g$', $x \mapsto gxg^{-1} : G \to G$, is an automorphism of $G$. An automorphism of this form is called an inner automorphism, and the remaining automorphisms are said to be outer" (Milne, p. 42).

# Prerequisites

- **Automorphism** — An inner automorphism is a particular type of automorphism
- **Conjugation** — Inner automorphisms are defined via conjugation

# Key Properties

1. $i_{gh} = i_g \circ i_h$, so $g \mapsto i_g : G \to \operatorname{Aut}(G)$ is a homomorphism
2. The kernel of this homomorphism is $Z(G)$, the centre of $G$
3. $G/Z(G) \simeq \operatorname{Inn}(G)$
4. $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$: for $\alpha \in \operatorname{Aut}(G)$, $\alpha \circ i_g \circ \alpha^{-1} = i_{\alpha(g)}$
5. If $\alpha$ is inner, it extends to every group containing $G$ as a subgroup (Aside 3.2)

# Construction / Recognition

## To construct:
1. Pick $g \in G$
2. Define $i_g(x) = gxg^{-1}$ for all $x \in G$

## To check if an automorphism is inner:
1. Determine if there exists $g \in G$ with $\alpha(x) = gxg^{-1}$ for all $x$

# Context & Application

Inner automorphisms measure how non-commutative a group is. They appear when analyzing normal subgroups (a subgroup is normal iff it is stable under all inner automorphisms) and in semidirect product constructions.

# Examples

**Example 1** (p. 42): For $G = \mathbb{F}_p^n$ (commutative), all nontrivial automorphisms are outer since $\operatorname{Inn}(G) = \{1\}$.

**Example 2** (p. 42): For the quaternion group $Q$, $\operatorname{Inn}(Q) \simeq Q/\langle a^2 \rangle \approx C_2 \times C_2$.

# Relationships

## Builds Upon
- **automorphism** — Inner automorphisms are automorphisms given by conjugation

## Enables
- **inner-automorphism-group** — The set $\operatorname{Inn}(G)$ of all inner automorphisms
- **outer-automorphism-group** — Defined as quotient $\operatorname{Aut}(G)/\operatorname{Inn}(G)$

## Contrasts With
- **outer-automorphism** — Automorphisms not of the form $x \mapsto gxg^{-1}$

# Common Errors

- **Error**: Assuming inner automorphisms of $G$ restrict to inner automorphisms of a normal subgroup $N$
  **Correction**: An inner automorphism of $G$ may restrict to an outer automorphism of $N$ (Example 3.16, p. 48)

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of groups", page 42.

# Verification Notes

- Definition source: Direct quote from p. 42
- Confidence: HIGH — explicit definition
- Uncertainties: None
