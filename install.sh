#!/bin/bash

# Claude 模型指纹检测 Skill 安装脚本

set -e

SKILL_NAME="模型指纹检测"
SKILL_DIR="$HOME/.claude/skills/$SKILL_NAME"
REPO_URL="https://raw.githubusercontent.com/bi-boo/claude-model-fingerprint/main"

echo "🔍 安装 Claude 模型指纹检测 Skill..."

# 创建目录
mkdir -p "$SKILL_DIR"

# 下载 SKILL.md
echo "📥 下载 SKILL.md..."
curl -fsSL "$REPO_URL/SKILL.md" -o "$SKILL_DIR/SKILL.md"

echo "✅ 安装完成！"
echo ""
echo "使用方法："
echo "  在 Claude Code 中输入: /模型指纹检测"
echo ""
