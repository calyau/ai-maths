---
concept: Block Code
slug: block-code
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 109
section: "8.1 Error-Detecting and Correcting Codes"
extraction_confidence: high
aliases:
  - "(n,m)-block code"
prerequisites: []
extends: []
related:
  - linear-code
  - group-code
contrasts_with: []
answers_questions:
  - "What is a block code?"
  - "What is an (n,m)-block code?"
---

# Quick Definition

An $(n, m)$-block code divides information into blocks of $m$ binary digits and encodes each into $n$ binary digits using an encoding function $E : \mathbb{Z}_2^m \to \mathbb{Z}_2^n$ (with $n > m$). The extra $n - m$ bits provide redundancy for error detection/correction.

# Core Definition

"A code is an $(n, m)$-*block code* if the information that is to be coded can be divided into blocks of $m$ binary digits, each of which can be encoded into $n$ binary digits. More specifically, an $(n, m)$-block code consists of an *encoding function* $E: \mathbb{Z}_2^m \to \mathbb{Z}_2^n$ and a *decoding function* $D: \mathbb{Z}_2^n \to \mathbb{Z}_2^m$" (Judson, p. 109). $E$ must be one-to-one.

# Prerequisites

No prerequisites beyond binary arithmetic.

# Key Properties

1. $m$ information bits encoded into $n$ total bits ($n > m$)
2. $n - m$ redundant bits for error handling
3. The encoding function $E$ must be injective (one-to-one)
4. If the code is error-correcting, then $D$ must be onto
5. A codeword is any element in the image of $E$

# Construction / Recognition

## To Construct:
1. Choose message length $m$ and codeword length $n > m$
2. Define an injective encoding function $E: \mathbb{Z}_2^m \to \mathbb{Z}_2^n$
3. Define a decoding function $D: \mathbb{Z}_2^n \to \mathbb{Z}_2^m$

# Context & Application

Block codes are the standard framework for coding theory. The ratio $m/n$ is the *code rate*, measuring efficiency.

# Examples

**Example 1** (p. 109): Even-parity ASCII is an $(8, 7)$-block code: 7 data bits + 1 parity bit.

# Relationships

## Enables
- **Linear Code** — A block code with additional algebraic structure
- **Group Code** — A block code that is also a group

# Common Errors

- **Error**: Defining $E$ so that two different messages encode to the same codeword
  **Correction**: $E$ must be one-to-one (injective)

# Common Confusions

- **Confusion**: Thinking $(n, m)$ means $n$ information bits and $m$ check bits
  **Clarification**: $m$ is the number of information bits and $n$ is the total codeword length

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.1, "Block Codes," page 109.

# Verification Notes

- Definition source: Direct from p. 109
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
