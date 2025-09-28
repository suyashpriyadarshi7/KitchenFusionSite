import './App.css';
import {RESTAURANT_MENU} from './assets/components/restaurantMenu.js';


function HeadBar({props}) {
  
  return(
    <>
      <div className="headbar">
        <h1>{props.title}</h1>
        
        <h3 style={{color: "black"}}>{props.subtitle}</h3>
        
      </div>
      
    </>
  )
}

function PageTitle({props}) {
  return (
    <div className="pagetitle">
      {props.pagetitle}
    </div>
  )
}


function ProductCategoryRow({props}) {

  function toTitleCase(str) {
    return str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }


  let items = [];
  for (let i = 0; i < props['items'].length; i++) {
    let key = props['items'][i][0].split(" ").join("-");
    if (typeof props['items'][i][1] === "string" || typeof props['items'][i][1] === "number") {
      let color = props['items'][i][2]=="v" ? 'green' : 'red';
      items.push(<tr key={key}>
        <td className='item-name' style={{'color': color}}>{toTitleCase(props['items'][i][0])}</td>
        <td> &#8377; {props['items'][i][1]}</td>
        {/* {todo: apply the description} */}

      </tr>)
    } else {
      let color = props['items'][i][2]=="v" ? 'green' : 'red';
      items.push(<tr key={key}>
        <td className='item-name' style={{'color': color}}>{toTitleCase(props['items'][i][0])}</td>
        <td> &#8377; {props['items'][i][1]["small"]}</td>
        <td> &#8377; {props['items'][i][1]["medium"]}</td>
        <td> &#8377; {props['items'][i][1]["large"]}</td>
      </tr>)
    }

    // if (Boolean(props['note'])) {
    //   items.push(
    //     <tr className='note-extra-cheese' key={toString(props['category']).concat('note')}>
    //       <td>{props['note'][0]}</td>
    //       <td>{props['note'][1]}</td>
    //     </tr>  
    //   )
    // }
  }

  let tableHeading;
  if (typeof props["items"][1][1] == "number") {
    tableHeading = (<tr><th className='tableheading'>Items</th><th className='tableheading'>Price</th></tr>)
  } else if (typeof props["items"][1][1] == "object") {
    let keys = Object.keys(props["items"][1][1]);
    let b = [];
    for (let i = 0; i < keys.length; i++) {
      b.push(<th className='tableheading' key={keys[i]}>{toTitleCase(keys[i])}</th>)
    }
    tableHeading = (
      <>
      <tr>
        <th className='tableheading' rowSpan={2}>Items</th>
        <th className='tableheading' colSpan={3} style={{textAlign: 'center'}}>Price</th>
      </tr>
        
        {b}
      <tr>

      </tr>
      </>
    );
    
  }

  return (
    
    // <tr className='categoryrow'>
    //   <td>
    //     {props["category"].toUpperCase()}
    //   </td>
    // </tr>
    <>
      <p className='categoryrow'>{props["category"].toUpperCase()}</p>
      <table>
        <tbody>
          {tableHeading}
          {items}
        </tbody>
      </table>
    </>
    
  )

}




function App() {
  let rows = []
  for (let i = 0; i < RESTAURANT_MENU.length; i++) {
    let item = <ProductCategoryRow props={RESTAURANT_MENU[i]} key={RESTAURANT_MENU[i]["category"]}></ProductCategoryRow>;
    rows.push(item);
  }
  

  return (
    <>
      <HeadBar props={{title: "Kitchen Fusion", subtitle: "Restaurant"}}></HeadBar>
      <PageTitle props={{pagetitle: "Menu"}}></PageTitle>
      {rows}
      
      
    </>
  )
}

export default App
