/**
 * bampli-api
 * The API for the Business Amplifier project.
 *
 * OpenAPI spec version: 1.0.0-oas3
 * Contact: josemotta@bampli.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/**
 * A representation of a Product.
 */
export interface Product { 
    /**
     * Auto-generated primary key field
     */
    product: string;
    name: string;
    active?: boolean;
    /**
     * This property is a reference to a Company
     */
    company: string;
}