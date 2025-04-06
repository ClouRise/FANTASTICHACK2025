<template>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>
                    <player fillColor="#ff0000" txt="1"></player>
                </th>
                <th>
                    <player fillColor="#5C7CFA" txt="2"></player>
                </th>
                <th>
                    <player fillColor="#FCC419" txt="3"></player>
                </th>
                <th>
                    <player fillColor="#94D82D" txt="4"></player>
                </th>
                <th>
                    <player fillColor="#CC5DE8" txt="5"></player>
                </th>
                <th>
                    <player fillColor="#FFFFFF" txt="6"></player>
                </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    <titlerow style="box-shadow: #EFDE22 0px 0px 3px 2px" num="1"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['1'] * 100)/ 100 }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['1'] * 100) / 100 }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['1'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['1'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['1'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['1'] * 100) / 100  }}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <titlerow style="box-shadow: #7A7A81 0px 0px 3px 2px" num="2"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['2'] * 100) / 100 }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['2'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['2'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['2'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['2'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['2'] * 100) / 100  }}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <titlerow style="box-shadow: #FF77004D 0px 0px 3px 2px" num="3"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['3'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['3'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['3'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['3'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['3'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['3'] * 100) / 100  }}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <titlerow num="4"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['4'] * 100 ) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['4'] * 100 ) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['4'] * 100 ) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['4'] * 100 ) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['4'] * 100 ) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['4'] * 100 ) / 100  }}</p>
                </td>
            </tr>
            <tr>
                <td>
                    <titlerow num="5"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['5'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['5'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['5'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['5'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['5'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['5'] * 100) / 100  }}</p>
                </td>
            </tr>
            <tr style="border: none;">
                <td>
                    <titlerow num="6"></titlerow>
                </td>
                <td>
                    <p>{{ Math.floor(prob['1']['6'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['2']['6'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['3']['6'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['4']['6'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['5']['6'] * 100) / 100  }}</p>
                </td>
                <td>
                    <p>{{ Math.floor(prob['6']['6'] * 100) / 100  }}</p>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import titlerow from './titlerow.vue';
import player from './player.vue';
import store from '@/store';
export default {
    data() {
        return {
            arr: store.state.arrOfRaced,
            objec: {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0
            },
            dateOfPlayers: []
        }
    },
    props: {
        prob: {
            type: Object,
            default: {}
        }
    },
    components: {
        titlerow,
        player
    },
    methods: {
        countOfPlace() {
            for (let pl = 1; pl <= 6; pl++) {
                this.objec = {
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    6: 0
                }
                for (let i = 0; i < this.arr.length; i++) {
                    if (this.arr[i]['1'] == pl) {
                        this.objec['1'] += 1
                    }
                    if (this.arr[i]['2'] == pl) {
                        this.objec['2'] += 1
                    }
                    if (this.arr[i]['3'] == pl) {
                        this.objec['3'] += 1
                    }
                    if (this.arr[i]['4'] == pl) {
                        this.objec['4'] += 1
                    }
                    if (this.arr[i]['5'] == pl) {
                        this.objec['5'] += 1
                    }
                    if (this.arr[i]['6'] == pl) {
                        this.objec['6'] += 1
                    }
                }
                this.dateOfPlayers[pl] = this.objec
            }
            console.log(this.dateOfPlayers)
        }
    }
}
</script>

<style scoped>
table {
    width: auto;
    height: auto;
    border-collapse: collapse;
}

tr {
    border-bottom: 1pt solid rgb(46, 46, 46);
}

td {
    padding-inline: 8px;
    padding-block: 8.8px;
    font-family: ubuntu-regular;
    color: white;
}

th {
    padding-inline: 8px;
    padding-block: 4.5px;
    font-family: ubuntu-regular;
    color: white;
}

p {
    text-align: center;
}
</style>