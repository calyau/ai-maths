---
# === CORE IDENTIFICATION ===
concept: Poisson Branching Process
slug: poisson-branching-process

# === CLASSIFICATION ===
category: probabilistic-method
subcategory: stochastic-processes
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 250
section: "VII.5 The Phase Transition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Galton-Watson process with Poisson offspring

# === TYPED RELATIONSHIPS ===
prerequisites:
  - phase-transition
extends: []
related:
  - branching-process-approximation
  - giant-component
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What branching process approximates the component growth in a random graph?"
---

# Quick Definition

A Poisson branching process with mean $c$ has $Z_0 = 1$ and each individual in generation $n$ produces $\text{Poisson}(c)$ offspring independently. For $c > 1$, the survival probability $p_\infty$ satisfies $e^{-cp_\infty} = 1 - p_\infty$.

# Core Definition

Let $Z_{ij}$, $i = 0, 1, \ldots$, $j = 1, 2, \ldots$, be independent Poisson random variables with mean $c$. Set $Z_0 = 1$, and $Z_{n+1} = Z_{n1} + Z_{n2} + \cdots + Z_{nZ_n}$. Then $Z_n$ is the size of the $n$th generation. **Theorem 19** (Bollobas, p. 250): For $c > 1$, the survival probability $p_\infty = \lim_{n\to\infty} \mathbb{P}(Z_n > 0)$ is the unique root of $e^{-cp_\infty} = 1 - p_\infty$ in $(0, 1)$.

# Prerequisites

- **Phase transition** -- The context in which the branching process arises

# Key Properties

1. For $c \le 1$: the process dies out almost surely ($p_\infty = 0$)
2. For $c > 1$: survival probability $p_\infty > 0$ satisfying $e^{-cp_\infty} = 1 - p_\infty$
3. $p_\infty$ equals $\gamma(c)$, the fractional size of the giant component
4. The recursion is $1 - p_{n+1} = e^{-cp_n}$, with $p_0 = 1$

# Construction / Recognition

## The Branching Process
1. Start with $Z_0 = 1$ individual
2. Each individual in generation $n$ independently produces $\text{Poisson}(c)$ offspring
3. $Z_{n+1}$ is the total offspring of all individuals in generation $n$
4. The process survives if $Z_n > 0$ for all $n$

# Context & Application

The Poisson branching process provides the exact asymptotic description of component growth in $G_{n,c/n}$. The survival/extinction dichotomy at $c = 1$ corresponds precisely to the phase transition in random graphs.

# Examples

**Example** (p. 250): The recursion $1 - p_{n+1} = e^{-cp_n}$ starting from $p_0 = 1$ converges to $p_\infty = \gamma$ satisfying $e^{-c\gamma} = 1 - \gamma$.

# Relationships

## Builds Upon
- **Phase transition** -- Setting

## Enables
- **Branching process approximation** -- The approximating model
- **Giant component** -- Size determination

## Related
- **Giant component** -- $\gamma = p_\infty$

## Contrasts With
- None

# Common Errors

- **Error**: Using Poisson offspring for supercritical analysis without truncation
  **Correction**: The Poisson approximation is valid for small components; large components require additional coupling arguments

# Common Confusions

- **Confusion**: Thinking the critical value $c = 1$ is a property specific to Poisson offspring
  **Clarification**: Criticality at mean 1 holds for all branching processes; the Poisson distribution arises specifically from the random graph model

# Source Reference

Chapter VII: Random Graphs, Section VII.5, Theorem 19, pages 250--251.

# Verification Notes

- Definition source: Direct from p. 250
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
