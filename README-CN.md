![export](https://github.com/MiniMax-AI/MiniMax-01/raw/main/figures/MiniMaxLogo-Light.png)

<div align="center" style="line-height: 1;">
  <a href="https://www.minimax.io" target="_blank" style="margin: 2px; color: var(--fgColor-default);">
    <img alt="Homepage" src="https://img.shields.io/badge/_Homepage-MiniMax-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://arxiv.org/abs/2501.08313" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📖_Paper-MiniMax--01-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://chat.minimax.io/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/_MiniMax_Chat-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.minimax.io/platform" style="margin: 2px;">
    <img alt="API" src="https://img.shields.io/badge/⚡_API-Platform-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>  
</div>
<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/🤗_Hugging_Face-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg" target="_blank" style="margin: 2px;">
    <img alt="WeChat" src="https://img.shields.io/badge/_WeChat-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.modelscope.cn/organization/MiniMax" target="_blank" style="margin: 2px;">
    <img alt="ModelScope" src="https://img.shields.io/badge/_ModelScope-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<div align="center" style="line-height: 1;">
   <a href="https://github.com/MiniMax-AI/MiniMax-MCP/blob/main/LICENSE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/_Code_License-MIT-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<p align="center" style="line-height: 1.5; font-size: 18px; margin: 4px auto; text-decoration: underline;"><a href="README.md">English Version</a></p>

<p align="center">
  专为 <b>coding-plan</b> 用户设计的 MiniMax 模型上下文协议(MCP)服务器，提供针对代码开发工作流优化的AI搜索和视觉分析API。与标准的 <a href="https://github.com/MiniMax-AI/MiniMax-MCP">MiniMax-MCP</a> 不同，此版本提供专门的编程工具（例如<code>coding_plan_search</code> 和 <code>coding_plan_vlm</code>），可无缝集成到 <a href="https://www.anthropic.com/claude">Claude Desktop</a>、<a href="https://www.cursor.so">Cursor</a>、<a href="https://codeium.com/windsurf">Windsurf</a>、<a href="https://github.com/openai/openai-agents-python">OpenAI Agents</a> 等 MCP 客户端，以增强您的编码体验。
</p>

## Documentation
- [English Documentation](README.md)

## 快速开始使用 MCP 客户端
1. 从[MiniMax国内开放平台](https://platform.minimaxi.com/user-center/basic-information/interface-key)｜[MiniMax国际开放平台](https://www.minimax.io/platform/user-center/basic-information/interface-key)获取你的 API 密钥。
2. 安装`uv`（Python包管理器），使用`curl -LsSf https://astral.sh/uv/install.sh | sh`安装或查看`uv` [仓库](https://github.com/astral-sh/uv)获取其他安装方法。
3. **重要提示: API的服务器地址和密钥在不同区域有所不同**，两者需要匹配，否则会有 `invalid api key` 的错误

|地区| 国际  | 国内  |
|:--|:-----|:-----|
|MINIMAX_API_KEY| 获取密钥 [MiniMax国际版](https://www.minimax.io/platform/user-center/basic-information/interface-key) | 获取密钥 [MiniMax](https://platform.minimaxi.com/user-center/basic-information/interface-key) |
|MINIMAX_API_HOST| https://api.minimax.io | https://api.minimaxi.com |


### Claude Desktop
前往`Claude > Settings > Developer > Edit Config > claude_desktop_config.json`包含以下内容：

```
{
  "mcpServers": {
    "MiniMax": {
      "command": "uvx",
      "args": [
        "minimax-coding-plan-mcp"
      ],
      "env": {
        "MINIMAX_API_KEY": "填写你的API密钥",
        "MINIMAX_MCP_BASE_PATH": "本地输出目录路径，如/User/xxx/Desktop",
        "MINIMAX_API_HOST": "填写API Host, https://api.minimaxi.com 或 https://api.minimax.io",
        "MINIMAX_API_RESOURCE_MODE": "可选配置，资源生成后的提供方式, 可选项为 [url|local], 默认为 url"
      }
    }
  }
}
```


⚠️ 注意：API Key需要与Host匹配。如果出现"API Error: invalid api key"错误，请检查您的API Host：
- 国际版Host：`https://api.minimax.io`
- 国内版Host：`https://api.minimaxi.com` 

如果你使用Windows，你需要在Claude Desktop中启用"开发者模式"才能使用MCP服务器。点击左上角汉堡菜单中的"Help"，然后选择"Enable Developer Mode"。


### Cursor
前往`Cursor -> Preferences -> Cursor Settings -> MCP -> Add new global MCP Server`添加上述配置。

你的MCP客户端现在可以通过Claude Desktop和Cursor等这些工具与MiniMax交互：

## Transport
我们支持两种传输方式: stdio and sse.
| stdio  | SSE  |
|:-----|:-----|
| 在本地部署运行 | 本地或云端部署均可  |
|通过 stdout 进行通信| 通过网络通信|
|输入：支持处理本地文件，或有效的URL资源| 输入: 若部署在云端，建议使用URL进行输入|

## 可用方法
| 方法  | 描述  |
|-|-|
|`coding_plan_search`|执行网络搜索并返回有机搜索结果以及相关搜索查询|
|`coding_plan_vlm`|基于文本提示使用AI分析图像，提取信息并回答关于图像的问题|

## 更新日志

### 2025年11月20日

#### 🆕 新增功能
- **网络搜索**: 新增 `coding_plan_search` 工具 - 执行网络搜索并获取有机搜索结果及相关搜索查询
- **视觉语言模型**: 新增 `coding_plan_vlm` 工具 - 基于文本提示使用AI分析图像

#### 📈 功能特性
- `coding_plan_search` - 搜索网络并获取结构化结果，包括标题、链接、摘要和相关搜索
- `coding_plan_vlm` - 分析来自URL或本地文件的图像，支持JPEG、PNG、GIF和WebP格式

## FAQ
### 1. invalid api key
请检查你获取的 API Key 和填写的 API Host 是否是同一地区的：
|地区| 国际  | 国内  |
|:--|:-----|:-----|
|MINIMAX_API_KEY| 获取密钥 [MiniMax国际版](https://www.minimax.io/platform/user-center/basic-information/interface-key) | 获取密钥 [MiniMax](https://platform.minimaxi.com/user-center/basic-information/interface-key) |
|MINIMAX_API_HOST| https://api.minimax.io | https://api.minimaxi.com

### 2. spawn uvx ENOENT
请在你的终端输入一下命令，查看uvx命令的绝对路径：
```sh
which uvx
```
如果得到如下的输出 (如：/usr/local/bin/uvx)，更新mcp配置 ("command": "/usr/local/bin/uvx"). 



## 使用示例

⚠️ 注意：使用这些工具可能会产生费用。

### 1. 网络搜索
使用 `coding_plan_search` 工具在网络上搜索信息：

<img src="https://cdn.hailuoai.video/moss/prod/2025-11-20-15/user/multi_chat_file/99ff15e3-e5d6-48e2-8216-38c6abf03c71.image/png" style="display: 
inline-block; vertical-align: middle; "/>

### 2. 图像分析
使用 `coding_plan_vlm` 工具通过AI分析图像：

<img src="https://cdn.hailuoai.video/moss/prod/2025-11-20-15/user/multi_chat_file/1f8174a2-68d5-4576-b886-86933eab5280.image/png" style="display: 
inline-block; vertical-align: middle; "/>
