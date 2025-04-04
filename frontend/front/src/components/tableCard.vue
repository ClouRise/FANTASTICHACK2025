<template>
    <table>
        <thead>
            <tr>
                <th></th>
                <th><player fillColor="#ff0000" txt="1"></player></th>
                <th><player fillColor="#5C7CFA" txt="2"></player></th>
                <th><player fillColor="#FCC419" txt="3"></player></th>
                <th><player fillColor="#94D82D" txt="4"></player></th>
                <th><player fillColor="#CC5DE8" txt="5"></player></th>
                <th><player fillColor="#FFFFFF" txt="6"></player></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><titlerow style="box-shadow: #EFDE22 0px 0px 5px 3px" num="1"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
            <tr>
                <td><titlerow style="box-shadow: #7A7A81 0px 0px 5px 3px" num="2"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
            <tr>
                <td><titlerow style="box-shadow: #FF77004D 0px 0px 5px 3px" num="3"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
            <tr>
                <td><titlerow num="4"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
            <tr>
                <td><titlerow num="5"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
            <tr>
                <td><titlerow num="6"></titlerow></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
                <td><p>15%</p></td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import titlerow from './titlerow.vue';
import player from './player.vue';
export default {
    components: {
        titlerow,
        player
    }
}
</script>

<style scoped>
table{
    width: auto;
    height: auto;
    border-collapse: collapse;
} 
tr{
    border-bottom: 1pt solid rgb(46, 46, 46);
}
td{
    padding-inline: 15px;
    padding-block: 8px;
    font-family: ubuntu-regular;
    color: white;
}
th{
    padding-inline: 15px;
    padding-block: 8px;
    font-family: ubuntu-regular;
    color: white;
}
p{
    text-align: center;
}
</style>