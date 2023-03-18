from enum import Enum


class SecTypes(Enum):
    AssetBacket = "Asset Backet"
    BankDebt = "Bank Debt"
    Bond = "Bond"
    BondConvertible = "Bond Convertible"
    BondCorporate = "Bond Corporate"
    BondGovernment = "Bond Government"
    BondSovereign = "Bond Sovereign"
    CumulativePreferred = "Cumulative Preferred"
    Depository = "Depository"
    DepositoryReceipt = "Depository Receipt"
    EquityPreffered = "Equity Preffered"
    Equity = "Equity"
    EquityRight = "Equity Right"
    EquityUnit = "Equity Unit"
    ExchangeTradedFund = "Exchange Traded Fund"
    Fund = "Fund"
    IndexAndNonEquityOption = "Index and Non-equity Option"
    PreferredConvertible = "Preferred Convertible"
    Warrant = "Warrant"


class SecTypeErrors(Enum):
    WRONG_SECTYPE = "Please, check that you use correct Sec_type"
