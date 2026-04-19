# 销售数据分析系统 - Code Wiki

## 1. 项目整体架构

本项目是一个基于 Python 和 Streamlit 框架构建的轻量级 Web 应用程序，专门用于销售数据的读取、清洗、统计与可视化分析。
系统采用模块化设计思想，前端交互和后端数据处理逻辑分离，主要包含以下四个核心层：

- **入口与展现层 (Presentation Layer)**：基于 Streamlit 实现，负责页面布局、文件上传、交互组件展示及结果渲染。
- **数据加载层 (Data Loading Layer)**：基于 Pandas 处理 Excel 文件，负责字段校验、数据类型转换以及脏数据清洗。
- **数据统计层 (Statistics Layer)**：负责对清洗后的有效数据进行多维度的聚合运算（如按商品、按日期的销量与销售额统计）。
- **数据可视化层 (Visualization Layer)**：基于 Plotly 构建，将统计结果转化为直观的交互式图表。

项目目录结构如下：
```text
/workspace/
├── src/                        # 源代码目录
│   ├── app.py                  # Streamlit 主入口文件
│   ├── sales_reader.py         # 数据读取与清洗模块
│   ├── sales_statistics.py     # 数据统计分析模块
│   └── sales_visualization.py  # 数据可视化展示模块
├── tests/                      # 单元测试目录
│   ├── test_sales_reader.py
│   ├── test_sales_statistics.py
│   └── test_sales_visualization.py
├── data/                       # 测试/示例数据目录
│   └── sales_january.xlsx
├── requirements.txt            # 项目依赖配置文件
└── README.md                   # 项目基本说明文档
```

## 2. 主要模块职责

| 模块名称 | 文件路径 | 职责描述 |
| :--- | :--- | :--- |
| **应用入口模块** | `src/app.py` | 系统的核心控制台。负责初始化 Streamlit 页面配置，构建上传组件，定义数据、统计和可视化三个核心 Tab 页的 UI 结构，并串联起其他处理模块。 |
| **数据读取模块** | `src/sales_reader.py` | 负责将上传的 Excel 文件转化为 Pandas DataFrame。执行关键的列名校验(`Date`, `Product`, `Quantity`, `Price`)、数据类型转换，并将数据切分为“有效数据”和“已剔除数据”。 |
| **数据统计模块** | `src/sales_statistics.py` | 提供一系列纯函数用于计算统计指标。包括整体概览（总销量、总销售额、商品种类数）、各商品维度的销售统计以及每日维度的销售统计。 |
| **数据可视化模块** | `src/sales_visualization.py` | 封装 Plotly 图表的生成逻辑。接收清洗后的数据，输出适用于 Streamlit 渲染的各类图表对象（柱状图、饼图、折线图、堆叠图等）。 |
| **自动化测试模块** | `tests/` | 包含针对各个业务模块的单元测试代码，确保核心逻辑（读取、统计、绘图）的正确性与鲁棒性。 |

## 3. 关键类与函数说明

项目主要采用函数式编程，未定义复杂的类结构。以下是核心函数的详细说明：

### 3.1 [app.py](file:///workspace/src/app.py)
- **`main()`**
  - **功能**：设置页面标题和全局样式，调用 `render_data_loading` 开始应用主流程。
- **`render_data_loading()`**
  - **功能**：渲染文件上传控件，接收用户上传的 Excel 文件。当文件上传后，依次调用数据读取、统计和可视化函数，并按 Tab 组织渲染结果。利用 `st.session_state` 暂存数据状态。

### 3.2 [sales_reader.py](file:///workspace/src/sales_reader.py)
- **`read_sales_data(file_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]`**
  - **功能**：读取 Excel 文件并清洗数据。
  - **逻辑**：检查是否包含必须列。将 `Quantity` 和 `Price` 转换为数值类型。过滤掉包含空值或 `Quantity < 0` 的无效数据。
  - **返回**：返回一个元组 `(valid_data, removed_data)`，分别为清洗后的有效数据集和被剔除的无效数据集。

### 3.3 [sales_statistics.py](file:///workspace/src/sales_statistics.py)
- **`get_statistics_summary(valid_data: pd.DataFrame) -> Dict`**
  - **功能**：计算全局统计概览（商品种类数、总销售量、总销售额）。
- **`calculate_product_statistics(valid_data: pd.DataFrame) -> pd.DataFrame`**
  - **功能**：按 `Product` 分组，计算每种商品的总销量和总销售额。
- **`calculate_daily_statistics(valid_data: pd.DataFrame) -> pd.DataFrame`**
  - **功能**：按 `Date` 分组，计算每日的总销售额。

### 3.4 [sales_visualization.py](file:///workspace/src/sales_visualization.py)
*(所有绘图函数均返回 `plotly.graph_objects.Figure` 对象)*
- **`visualize_product_statistics(valid_data: pd.DataFrame)`**：生成各商品销售量的柱状图。
- **`visualize_product_sales(valid_data: pd.DataFrame)`**：生成各商品销售额占比的饼图。
- **`visualize_daily_statistics(valid_data: pd.DataFrame)`**：生成每日销售额趋势的折线图。
- **`visualize_daily_sales_quantity(valid_data: pd.DataFrame)`**：生成每日销售量的柱状图。
- **`visualize_stacked_bar_chart(valid_data: pd.DataFrame)`**：生成每日各产品销售额的堆叠柱状图。
- **`visualize_combined_analysis(valid_data: pd.DataFrame)`**：生成包含销售量柱状图和销售额饼图的组合图表。

## 4. 依赖关系

项目运行依赖于以下第三方 Python 库（详情见 [requirements.txt](file:///workspace/requirements.txt)）：

- **核心运行框架**
  - [streamlit](https://streamlit.io/) (`>=1.0.0`)：提供 Web 界面和交互式组件支持。
- **数据处理与分析**
  - pandas（隐式依赖，通常随 Streamlit 安装或通过 openpyxl 一起使用）：强大的数据结构和分析工具。
  - openpyxl (`>=3.0.0`)：用于读取和解析 `.xlsx` / `.xls` 格式的 Excel 文件。
- **数据可视化**
  - [plotly](https://plotly.com/python/) (`>=5.0.0`)：用于生成丰富的、可交互的数据可视化图表。
- **开发与测试工具**
  - pytest (`>=7.0.0`)：用于编写和运行单元测试。
  - black (`>=22.0.0`)：代码格式化工具。
  - flake8 (`>=4.0.0`)：代码静态规范检查工具。

## 5. 项目运行方式

### 5.1 环境准备与依赖安装
确保系统中已安装 Python 3.7+。在项目根目录下，执行以下命令安装依赖库：
```bash
pip install -r requirements.txt
```

### 5.2 启动 Web 应用程序
在项目根目录执行以下命令启动 Streamlit 服务：
```bash
streamlit run src/app.py
```
启动成功后，终端将输出本地访问地址（通常为 `http://localhost:8501`）。在浏览器中打开该地址，即可使用销售数据分析系统。

### 5.3 运行单元测试
在开发或修改代码后，可以通过 pytest 运行单元测试来确保系统功能正常：
```bash
pytest
```
这将自动发现并执行 `tests/` 目录下所有的测试用例。