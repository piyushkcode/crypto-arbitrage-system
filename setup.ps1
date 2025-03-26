# PowerShell Script for Windows

$dir = "D:\\Data Analysis Projects\\crypto-arbitrage-system"

# Create directories
$folders = @(
    "$dir\\backend\\app\\services", "$dir\\backend\\app\\utils", "$dir\\backend\\app\\middleware",
    "$dir\\backend\\config", "$dir\\backend\\database\\schemas", "$dir\\backend\\database\\models",
    "$dir\\backend\\exchanges", "$dir\\backend\\machine_learning\\models", "$dir\\backend\\tests",
    "$dir\\frontend\\public", "$dir\\frontend\\src\\components\\Layout", "$dir\\frontend\\src\\components\\Dashboard",
    "$dir\\frontend\\src\\components\\Charts", "$dir\\frontend\\src\\components\\Common", "$dir\\frontend\\src\\pages",
    "$dir\\frontend\\src\\contexts", "$dir\\frontend\\src\\hooks", "$dir\\frontend\\src\\services",
    "$dir\\frontend\\src\\utils", "$dir\\frontend\\src\\styles", "$dir\\data\\historical_prices",
    "$dir\\data\\ml_training_data", "$dir\\docs", "$dir\\scripts"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

# Create backend files
$backendFiles = @(
    "$dir\\backend\\requirements.txt", "$dir\\backend\\README.md",
    "$dir\\backend\\app\\__init__.py", "$dir\\backend\\app\\main.py", "$dir\\backend\\app\\routes.py",
    "$dir\\backend\\app\\services\\__init__.py", "$dir\\backend\\app\\services\\arbitrage_service.py",
    "$dir\\backend\\app\\services\\exchange_service.py", "$dir\\backend\\app\\services\\trading_service.py",
    "$dir\\backend\\app\\services\\machine_learning_service.py", "$dir\\backend\\app\\utils\\__init__.py",
    "$dir\\backend\\app\\utils\\api_client.py", "$dir\\backend\\app\\utils\\websocket_handler.py",
    "$dir\\backend\\app\\utils\\error_handler.py", "$dir\\backend\\app\\middleware\\__init__.py",
    "$dir\\backend\\app\\middleware\\auth_middleware.py", "$dir\\backend\\app\\middleware\\rate_limiter.py",
    "$dir\\backend\\config\\__init__.py", "$dir\\backend\\config\\settings.py", "$dir\\backend\\config\\logging_config.py",
    "$dir\\backend\\database\\__init__.py", "$dir\\backend\\database\\connection.py",
    "$dir\\backend\\database\\schemas\\__init__.py", "$dir\\backend\\database\\schemas\\user_schema.py",
    "$dir\\backend\\database\\schemas\\trade_schema.py", "$dir\\backend\\database\\schemas\\exchange_schema.py",
    "$dir\\backend\\database\\schemas\\arbitrage_schema.py", "$dir\\backend\\database\\models\\__init__.py",
    "$dir\\backend\\database\\models\\user_model.py", "$dir\\backend\\database\\models\\trade_model.py",
    "$dir\\backend\\database\\models\\exchange_model.py", "$dir\\backend\\database\\models\\arbitrage_model.py",
    "$dir\\backend\\exchanges\\__init__.py", "$dir\\backend\\exchanges\\binance.py", "$dir\\backend\\exchanges\\kraken.py",
    "$dir\\backend\\exchanges\\kucoin.py", "$dir\\backend\\exchanges\\base_exchange.py",
    "$dir\\backend\\machine_learning\\__init__.py", "$dir\\backend\\machine_learning\\data_preprocessing.py",
    "$dir\\backend\\machine_learning\\training_pipeline.py", "$dir\\backend\\machine_learning\\models\\__init__.py",
    "$dir\\backend\\machine_learning\\models\\lstm_model.py", "$dir\\backend\\machine_learning\\models\\random_forest_model.py",
    "$dir\\backend\\tests\\__init__.py", "$dir\\backend\\tests\\test_arbitrage.py",
    "$dir\\backend\\tests\\test_exchanges.py", "$dir\\backend\\tests\\test_ml_models.py"
)

# Create frontend files
$frontendFiles = @(
    "$dir\\frontend\\package.json", "$dir\\frontend\\README.md",
    "$dir\\frontend\\public\\index.html", "$dir\\frontend\\public\\favicon.ico",
    "$dir\\frontend\\src\\App.js", "$dir\\frontend\\src\\index.js",
    "$dir\\frontend\\src\\components\\Layout\\Sidebar.js", "$dir\\frontend\\src\\components\\Layout\\Navbar.js",
    "$dir\\frontend\\src\\components\\Layout\\MainLayout.js", "$dir\\frontend\\src\\components\\Dashboard\\PerformanceChart.js",
    "$dir\\frontend\\src\\components\\Dashboard\\TopOpportunitiesTable.js", "$dir\\frontend\\src\\components\\Dashboard\\SummaryCards.js",
    "$dir\\frontend\\src\\components\\Dashboard\\WalletDistributionChart.js", "$dir\\frontend\\src\\components\\Dashboard\\AIMarketPredictions.js",
    "$dir\\frontend\\src\\components\\Dashboard\\AnalyticsCompliance.js", "$dir\\frontend\\src\\components\\Charts\\LineChart.js",
    "$dir\\frontend\\src\\components\\Charts\\PieChart.js", "$dir\\frontend\\src\\components\\Charts\\AreaChart.js",
    "$dir\\frontend\\src\\components\\Common\\SearchBar.js", "$dir\\frontend\\src\\components\\Common\\SettingsButton.js",
    "$dir\\frontend\\src\\components\\Common\\ProfileBadge.js", "$dir\\frontend\\src\\pages\\Dashboard.js",
    "$dir\\frontend\\src\\pages\\MarketData.js", "$dir\\frontend\\src\\pages\\Opportunities.js",
    "$dir\\frontend\\src\\pages\\TradeExecution.js", "$dir\\frontend\\src\\pages\\AiCenter.js",
    "$dir\\frontend\\src\\pages\\WalletManager.js", "$dir\\frontend\\src\\pages\\PerformancePage.js",
    "$dir\\frontend\\src\\contexts\\AuthContext.js", "$dir\\frontend\\src\\contexts\\DashboardContext.js",
    "$dir\\frontend\\src\\hooks\\useWebSocket.js", "$dir\\frontend\\src\\hooks\\useApiData.js",
    "$dir\\frontend\\src\\services\\dashboardService.js", "$dir\\frontend\\src\\services\\arbitrageService.js",
    "$dir\\frontend\\src\\services\\walletService.js", "$dir\\frontend\\src\\utils\\formatters.js",
    "$dir\\frontend\\src\\utils\\constants.js", "$dir\\frontend\\src\\styles\\tailwind.css",
    "$dir\\frontend\\src\\styles\\theme.css", "$dir\\frontend\\src\\styles\\dashboard.css"
)

$rootFiles = @("$dir\\.env", "$dir\\.gitignore", "$dir\\docker-compose.yml", "$dir\\Dockerfile", "$dir\\README.md")

foreach ($file in ($backendFiles + $frontendFiles + $rootFiles)) {
    New-Item -ItemType File -Path $file -Force | Out-Null
}

# Initialize Git and open in VS Code
Set-Location "$dir"
git init
git add .
git commit -m "Initial commit"
echo "Project structure created successfully!"
code .
