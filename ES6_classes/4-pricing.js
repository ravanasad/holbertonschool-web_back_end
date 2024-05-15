import Currency from "./3-currency";

export default class Pricing
{
    constructor(amount, currency)
    {
        this._amount = amount;
        this._currency = currency;
    }

    get amount()
    {
        return this._amount
    }

    set amount(newAmount)
    {
        if (typeof newAmount === 'number')
            this._amount = newAmount;
        else
            throw new TypeError('Amount must be a number');
    }

    get currency()
    {
        return this._currency;
    }

    set currency(newCurrency)
    {
        if (newCurrency instanceof Currency)
            this._currency = newCurrency;
        else
            throw new TypeError('Currency must be a Currency');
    }

    displayFullPrice()
    {
        return `${this._amount} ${this._currency.displayFullCurrency()}`
    }

    static convertPrice(amount, conversionRate)
    {
        return amount * conversionRate;
    }
}