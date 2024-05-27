import { Route, Routes } from 'react-router-dom';
import {Lung} from "./Components/Lung/Lung";
import { Breast } from './Components/Breast/Breast';
import { Kidney } from './Components/Kidney/Kidney';
import { Brain } from './Components/Brain/Brain'
import Main from "./Components/Main"
import { BrowserRouter  } from "react-router-dom";
import Location from './Components/Location/Location';
import AboutUs from './Components/AboutUs/AboutUs';


function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element={<><Main /> </>}/>
        <Route path="/lung" element={<><Lung />  </>} />
        <Route path="/breast" element={<><Breast/> </>}/>
        <Route path="/Kidney" element={<><Kidney/> </>}/>
        <Route path="/brain" element={<><Brain/> </>}/>
        <Route path="/location" element={<><Location/> </>}/>
        <Route path="/aboutus" element={<><AboutUs/> </>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;