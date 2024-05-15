export default class Building
{
    constructor(sqft)
    {
        if (this.constructor !== Building && this.evacuationWarningMessage !== "function")
        {
            throw new TypeError('Class Building cannot be instantiated');
        }
        this._sqft = sqft;
    }

    get sqft()
    {
        return this._sqft;
    }

    set sqft(newSqft)
    {
        if (typeof newSqft === 'number')
            this._sqft = newSqft;
        else
            throw new TypeError('Sqft must be a number');
    }
}