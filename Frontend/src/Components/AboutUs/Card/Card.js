// Card.js

import React from 'react';

export default function Card() {
    return (
        <div className="card-container hover:bg-gray-100 transition-transform duration-300 transform hover:scale-105">
            <div className="h-52 ml-48 float-left -mt-10 w-96 flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-2xl">
                <div className="p-6">
                    <h5 className="text-center mr-4 mb-2 block font-sans text-xl font-semibold text-blue-gray-900 antialiased">
                        Reach Us At
                    </h5>
                    <ul>
                        <li className="mt-2">
                            <span><i className="fa fa-phone mr-2"></i> </span>
                            +91-9908185413
                        </li>
                        <li className="mt-2">
                            <span><i className="fa fa-envelope mr-2"></i> </span>
                            <span>healthcare@org.in</span>
                        </li>
                        <li className="mt-2">
                            <span><i className="fa-solid fa-map-pin mr-2"></i> </span>
                            Vasavi College of Engineering<br />
                            <span className="pl-2">
                                Ibrahimbagh, Hyderabad
                            </span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    );
}
