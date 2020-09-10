import React from 'react';
const Pagination=(props)=>{
const PageNumbers=[];
console.log("yes"+props.totalpost);
for(let i=1;i<=Math.ceil((props.totalpost)/(props.postsPerPage));i++)
{
PageNumbers.push(i);
}
return(
<div>
<nav>
<ul className="pagination">
{PageNumbers.map(no => (
<li className="page-item" key={no}>
<a onClick={()=> props.paginate(no)}  className="page-link">{no}</a>
</li>
))}

</ul>
</nav>

</div>
);	
}
export default Pagination;