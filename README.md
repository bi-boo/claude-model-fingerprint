# Claude 模型指纹检测 Skill

通过自省式分析检测当前 API 是否为真实 Claude 模型，或是否存在多层封装和提示词冲突。

## 功能特点

- 🔍 **自省式检测** - 不调用外部 API，分析内部系统提示词结构
- 🎯 **五大检测维度** - 身份声明、工具生态、元数据、知识能力、嵌套层级
- ✅ **智能识别** - 区分合法封装（如 Claude Code）和可疑封装
- 📊 **结构化报告** - 生成详细的检测报告

## 安装方法

### 方法 1：直接复制

```bash
# 创建 Skill 目录
mkdir -p ~/.claude/skills/模型指纹检测

# 下载 SKILL.md
curl -o ~/.claude/skills/模型指纹检测/SKILL.md \
  https://raw.githubusercontent.com/bi-boo/claude-model-fingerprint/main/SKILL.md
```

### 方法 2：Git Clone

```bash
cd ~/.claude/skills/
git clone https://github.com/bi-boo/claude-model-fingerprint.git 模型指纹检测
```

## 使用方法

在 Claude Code 中输入：

```
/模型指纹检测
```

或者在对话中提到"检测模型指纹"、"验证 API 真实性"等关键词。

## 检测维度

### 1. 身份声明一致性
- 检测多重身份冲突
- 识别反向指令
- 分析身份声明层级

### 2. 工具生态分析
- 验证工具列表合法性
- 识别非标准扩展
- 区分用户自定义工具

### 3. 元数据检查
- 分析 billing header
- 检查会话追踪机制
- 验证 Machine ID

### 4. 知识能力验证
- 测试知识截止日期
- 验证 Constitutional AI 理解
- 检查 Anthropic 认知深度

### 5. 嵌套层级分析
- 识别提示词注入层级
- 绘制封装结构图
- 评估合法性

## 输出示例

```markdown
# 模型指纹检测报告

## 最终结论
**模型类型：** 封装的 Claude
**底层模型：** Claude Sonnet 4.6 ✅
**可信度：** 高

## 建议
当前使用的是真实 Claude API，经过 Claude Code 合法封装。
```

## 适用场景

- 怀疑 API 可能不是官方 Claude
- 需要验证模型身份和来源
- 检测是否存在中转或封装层
- 分析提示词注入和冲突

## 技术原理

本 Skill 采用**自省式检测**方法：
- 不依赖外部 API 调用
- 直接分析系统提示词结构
- 识别配置特征和元数据
- 通过知识验证确认模型身份

## 兼容性

- ✅ Claude Code (所有版本)
- ✅ 其他支持 Skill 的 Claude 客户端
- ✅ 任何基于 Claude API 的封装工具

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 作者

Created by [Your Name]

## 相关链接

- [Anthropic 官方文档](https://docs.anthropic.com)
- [Claude API 参考](https://docs.anthropic.com/claude/reference)
- [Model Context Protocol](https://modelcontextprotocol.io)
